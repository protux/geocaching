from itertools import permutations

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
A = 0
B = 1
C = 2
D = 3
E = 4
F = 5
G = 6
H = 7
I = 8
J = 9

def get11():
    return nums[A] * 100 + nums[B] * 10 + nums[A]

def get12():
    return nums[C] * 100 + nums[D] * 10 + nums[A]

def get13():
    return nums[D] * 100 + nums[E] * 10 + nums[F]

def get21():
    return nums[C] * 100 + nums[G] * 10 + nums[H]
    
def get22():
    return nums[E] * 10 + nums[I]
    
def get23():
    return nums[E] * 100 + nums[F] * 10 + nums[F]
    
def get31():
    return nums[C] * 100 + nums[J] * 10 + nums[G]

def get32():
    return nums[C] * 100 + nums[A] * 10 + nums[B]

def get33():
    return nums[A] * 100 + nums[E] * 10 + nums[F]

def printResult():
    print("A: %d, B: %d, C: %d, D: %d, E: %d, F: %d, G: %d, H: %d, I: %d, J: %d" % (nums[A], nums[B], nums[C], nums[D], nums[E], nums[F], nums[G], nums[H], nums[I], nums[J]))
    print("N 52° 23.%d%d%d E 013° 48.%d%d%d" % (nums[C], nums[J], nums[G], nums[D], nums[H], nums[F]))
    
def check():
    return get11() + get12() == get13() and \
    get21() + get22() == get23() and \
    get31() + get32() == get33() and \
    get11() - get21() == get31() and \
    get12() - get22() == get32() and \
    get13() - get23() == get33()

#def allPermutations(elements):
#    for permutation in allPermutations(elements[1:]):
#        for i in range(len(elements)):
#            yield permutation[:i] + elements[0:1] + permutation[i:]

if __name__ == "__main__":
    result = permutations(nums)
    for res in result:
        A = res[0]
        B = res[1]
        C = res[2]
        D = res[3]
        E = res[4]
        F = res[5]
        G = res[6]
        H = res[7]
        I = res[8]
        J = res[9]
        if check():
            printResult()
            break
