def problem11(numbers):
    total = 0
    for n in numbers:
        total += n

    return total


print problem11([1, 2,3])

def problem12(numbers):
    i = 0
    total = 0
    while i < len(numbers):
       total += numbers[i] 
       i += 1
    return total


print problem12([1,2,3])

def problem13(numbers):
    total += numbers


def problem2(one_list, two_list):
    a = []
    for x,y in zip(one_list, two_list):
        a.append(x)
        a.append(y)
    return a


print problem2(['b', 'c'], [1, 2])


def problem3():
    l = [0, 1]
    i = 1 
    while i < 99: 
        temp = l[i] + l[i-1]
        l.append(temp)
        i += 1
    return l

print problem3()



def problem4(numbers):
    new_l = sorted([str(x) for x in numbers])
    new_l.reverse()
    return  int(''.join(new_l))

print problem4([5, 6, 79])

from itertools import combinations
def problem5():
    numbers = [1,2,3,4,5,6,7,8,9]
    for r in xrange(len(numbers)):
        for per in combinations(numbers, r):
            yield per

