import workerpool, time, os

from PIL import Image

import smtplib
from email.mime.text import MIMEText
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate


URL = "http://188.64.45.96/listing/kreis.php"
REFERENCE_IMAGE = 'non_changing_area.png'
SAVE_FOLDER = 'uhr/'
RELEVANT_FOLDER = 'uhr/relevant/'
NUM_SOCKETS = 10
NUM_WORKERS = 20
ERROR_THRESHOLD = 10

EMAIL = '<your_address>@gmx.de'
PASSWORD = '<your_mail_password>'
RECEIVER = ['<receiver_email>']
SUBJECT = 'Es wurde eine Anomalie gefunden!'
MESSAGE = 'Die Suche nach den Koordinaten war erfolgreich.'
SERVER = 'mail.gmx.net'

workers = workerpool.WorkerPool(size=NUM_WORKERS)

exit = False

class Worker(workerpool.Job):
    def __init__(self, url, timestamp):
        self.url = url
        self.ts = timestamp
        self.filename = "%s%d%02d%02d%02d%02d%02d.jpg" % (SAVE_FOLDER, self.ts.tm_year, self.ts.tm_mon, self.ts.tm_mday, self.ts.tm_hour, self.ts.tm_min, self.ts.tm_sec)
        
    def run(self):
        self.downloadImage()
        if self.checkImageDeletion(self.filename, REFERENCE_IMAGE):
            os.remove(self.filename)
        else:
            self.sendMail()
            os.rename(self.filename, '%s%s' % (RELEVANT_FOLDER, os.path.basename(self.filename)))
    
    def checkImageDeletion(self, filename, referenceFile):
        oImage = Image.open(filename)
        nsaImage = Image.open(referenceFile)
        
        errorPixels = []
        for x in range(0, oImage.width):
            for y in range(0, oImage.height):
                irrelevant = nsaImage.getpixel((x,y))[3] != 255
                if not irrelevant:
                    pixel = oImage.getpixel((x,y))
                    if pixel[0] < 240 or pixel[1] < 240 or pixel[2] < 240:
                        errorPixels += [oImage.getpixel((x,y))]
        if len(errorPixels) > ERROR_THRESHOLD:
            return False
        else:
            return True
            
    def sendMail(self):
        msg = MIMEMultipart(
            From=EMAIL,
            To=", ".join(RECEIVER),
            Date=formatdate(localtime=True),
            Subject=SUBJECT
        )
        msg.attach(MIMEText(MESSAGE))
        
        with open(self.filename, "rb") as fil:
            msg.attach(MIMEApplication(
                fil.read(),
                Content_Disposition='attachment; filename="%s"' % basename(self.filename),
                Name=basename(self.filename)
            ))

        try:
            server = smtplib.SMTP(SERVER)
            server.starttls()
            server.login(EMAIL,PASSWORD)
            server.sendmail(EMAIL, RECEIVER, msg.as_string())         
            print ("Successfully sent email")
        except Exception as e:
            print (e)   
    
    def downloadImage(self):
        try:
            os.system("wget -qO %s %s" % (self.filename, self.url))
        except Exception as e:
            print(e)    
          
if __name__ == '__main__':

    second = -1
    try:
        while(not exit):
            try:
                time.sleep(0.25)
            except KeyboardInterrupt:
                exit = True
            timestamp = time.gmtime()
            sec = timestamp.tm_sec
            if sec != second:
                second = sec
                workers.put(Worker(URL, timestamp))
    except Exception as e:
        print(e)
    finally:
        workers.shutdown()
        workers.wait()
