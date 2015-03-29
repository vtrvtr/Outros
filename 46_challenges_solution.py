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


def problem_7(string):  # Returns reversed string
    return ''.join([char for char in reversed(string)])


def problem_8(string):  # Returns True if word is palindrome, uses problem_7
    return True if string == problem_7(string) else False


def problem_9(token, list_of_things):
    for thing in list_of_things:
        if thing == token:
            return True
    return False


def problem_10(list_one, list_two):
    for item1 in list_one:
        for item2 in list_two:
            if item1 == item2:
                return True
    return False

def problem_11(number_to_multiply, char):
    result = []
    for number in range(number_to_multiply):
        result.append(char)
    return ''.join(result)

def problem_12(histogram_numbers):
    result = []
    for number in histogram_numbers: 
        result.append([problem_11(number, '*')])
    return '\n'.join(''.join(inner_list) for inner_list in result)


def test():
    print problem_1(3, 4)
    print problem_2(13, 8, 24)
    print problem_3([2, 2, 2, 2, 2, 2])
    print problem_4('b')
    print problem_5('this is fun')
    print problem_6([2, 2], '+')
    print problem_6([3, 3, 3], '*')
    print problem_7('aya lmao')
    print problem_8('radar')
    print problem_9('a', ['2', 2, 45, 'd'])
    print problem_10([1, 2, 3, 4, True], ['lol', 1])
    print problem_11(3, 's')
    print problem_12([2,3,6])
test()
