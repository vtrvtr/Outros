def problem_1(a, b):    # Returns the max number
    return a if a > b else b


def problem_2(a, b, c):  # Returns max of 3 numbers
    max_n = a if a > b else b
    return max_n if max_n > c else c


def problem_3(a):  # Returns lenght of a list
    return [i + 1 for i, _ in enumerate(a)][-1]


def problem_4(char):  # Returns true if vowel else False
    return True if char in 'aeiou' else False


def problem_5(string):
    new_string = []
    for char in string:
        if char not in 'aeiou' and char is not ' ':
            new_string.append('{}{}{}'.format(char, 'o', char))
        else:
            new_string.append(char)
    return ''.join(new_string)


def problem_6(list_of_numbers, action):
    if action == '+':
        result = 0
        for number in list_of_numbers:
            result += number
        return result
    elif action == '*':
        result = 1
        for number in list_of_numbers:
            result *= number
        return result
    else:
        'Usage: problem_6 list of numbers + * for the action'


def test():
    print problem_1(3, 4)

    print problem_2(13, 8, 24)

    print problem_3([2, 2, 2, 2, 2, 2])

    print problem_4('b')

    print problem_5('this is fun')
    print problem_6([2,2], '+')
    print problem_6([3,3,3], '*') 
test()
