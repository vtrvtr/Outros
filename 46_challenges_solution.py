from collections import Counter as counter
import re
from itertools import permutations
from itertools import combinations
from tabulate import tabulate
import pyttsx
import time
from pprint import pprint
from string import ascii_lowercase


def problem_1(a, b):    # Returns the max number
    return a if a > b else b


def problem_2(a, b, c):  # Returns max of 3 numbers
    max_n = a if a > b else b
    return max_n if max_n > c else c


def problem_3(a):  # Returns lenght of a list
    return [i + 1 for i, _ in enumerate(a)][-1]


def problem_4(char):  # Returns true if vowel else False
    return True if char in 'aeiou' else False


def problem_5(string):  # Do some strange shit from Sweden with a word
    new_string = []
    for char in string:
        if char not in 'aeiou' and char is not ' ':
            new_string.append('{}{}{}'.format(char, 'o', char))
        else:
            new_string.append(char)
    return ''.join(new_string)


def problem_6(list_of_numbers, action):  # Multiply or add numbers in a list
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


def problem_9(token, list_of_things):  # Check if token is in the list
    for thing in list_of_things:
        if thing == token:
            return True
    return False


# Check if list 1 and list 2 have any items in common
def problem_10(list_one, list_two):
    for item1 in list_one:
        for item2 in list_two:
            if item1 == item2:
                return True
    return False


def problem_11(number_to_multiply, char):  # Return char N times
    result = []
    for number in range(number_to_multiply):
        result.append(char)
    return ''.join(result)


# Makes a histogram using problem 11 function
def problem_12(histogram_numbers):
    result = []
    for number in histogram_numbers:
        result.append([problem_11(number, '*')])
    return '\n'.join(''.join(inner_list) for inner_list in result)


# compare every number in a list and return the biggest
def problem_13(list_of_numbers):
    max_n = 0
    for n in list_of_numbers:
        if n > max_n:
            max_n = n
    return max_n


def problem_14(list_of_words):  # Return the len of each word of a list
    len_of_words = []
    for word in list_of_words:
        len_of_words.append(len(word))
    return len_of_words


# Returns the len of the biggest word using problems 14 func
def problem_15(list_of_words):
    return max(problem_14(list_of_words))


# Returns the words bigger than max_size
def problem_16(list_of_words, max_size):
    return [word for word in list_of_words if len(word) > max_size]


def problem_17(phrase):  # Returns True is whole phrase is a palindrome
    phrase = phrase.replace(' ', '')
    reversed_phrase = ''.join([char.lower() for word in reversed(
        phrase) for char in reversed(word) if char not in ' !.,?'])
    return True if phrase.lower() == reversed_phrase else False


# Check if phrase has all letters of the alphabet, aka, it's a pagram
def problem_18(phrase):
    for char in phrase.lower():
        if char not in 'abcdefghijklmnopqrstuvxwzy ':
            print char
            return False
    return True


def problem_19():  # Loops to sing the 99 beers gon
    for number in reversed(range(99)):
        print '''{} bottles of beer on the wall, {} bottles of beer.
        Take one down, pass it around, {} bottles of beer on the wall.'''.format(number + 1, number + 1, number)


def problem_20(words):  # Translates from english to swedish
    word_dict = {"merry": "god", "christmas": "jul", "and": "och",
                 "happy": "gott", "new": "nytt", "year": "ar"}
    return ' '.join([word_dict[key] if key in word_dict else key for key in words.lower().split()])


def problem_21(phrase):  # Count how many tokens are in a phrase
    return counter(phrase)


def problem_22(cipher, action):  # Ceaser cipher
    key = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u',
           'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c',
           'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k',
           'y': 'l', 'z': 'm', 'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S',
           'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A',
           'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I',
           'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}
    if action == 'decode':
        decoded = []
        for char in cipher:
            if char == ' ':
                decoded.append(char)
            for k, v in key.items():
                if v == char:
                    decoded.append(k)
        return ''.join(decoded)
    elif action == 'encode':
        return [key[k] if k is not ' ' else ' ' for k in cipher]
    else:
        return 'Usage: cipher decode/encode '


def problem_23(phrase):  # Correct mistakes in a phrase
    if '  ' in phrase:
        phrase = phrase.replace('  ', ' ')
    i_dot = phrase.find('.')

    if phrase[i_dot + 1] is not ' ':
        first_half_of_phrase = phrase[:i_dot + 1]
        second_half_of_phrase = phrase[i_dot + 1:]
        return '{} {}'.format(first_half_of_phrase, second_half_of_phrase)

    return phrase


def problem_24(verb):  # transforms verb into the 3rd person
    if verb.endswith('y'):
        return '{}{}'.format(verb[:-1], 'ies')
    elif verb.endswith(('o', 'ch', 's', 'sh', 'x', 'z')):
        return '{}{}'.format(verb, 'es')
    else:
        return '{}{}'.format(verb, 's')


def problem_25(verb):  # transforms in continuum form
    vowels = 'aeiou'
    if verb.endswith('e') and verb not in ['be', 'see', 'flee', 'knee', 'lie']:
        return '{}{}'.format(verb[:-1], 'ing')
    elif verb.endswith('ie'):
        return '{}{}'.format(verb[:-2], 'ying')
    elif verb[-1] not in vowels and verb[-2] in vowels and verb[-3] not in vowels:
        return '{}{}{}'.format(verb, verb[-1], 'ing')
    else:
        return '{}{}'.format(verb, 'ing')


# Get the largest value in a list using reduce or just a normal list comp
def problem_26(list_of_numbers):
    # f = lambda x,y: x if (x>y) else y
    # return reduce(f, list_of_numbers)
    return [a if a > b else b for a, b in zip(list_of_numbers, list_of_numbers[1:])][-1]


def problem_27(list_of_words):  # returns the biggest word
    return [a if len(a) > len(b) else b for a, b in zip(list_of_words, list_of_words[1:])][-1]


# returns words bigger the max_size, much like problem 16
def problem_28(list_of_words, max_size):
    return [word for word in list_of_words if len(word) > max_size]


# Uses problem 17 to print phrases that are palindromes in a file
def problem_29(path_to_file):
    with open(path_to_file, 'r') as f:
        for line in f:
            if problem_17(line.rstrip()):
                print line


# Using itertools.combinations finds that are the same as some other world
# of the list  backwards
def problem_30(path_to_file):
    with open(path_to_file, 'r') as f:
        for line in combinations(f, 2):
            if line[0].rstrip() == problem_7(line[1].rstrip()):
                print "{} {}".format(line[0].rstrip(), line[1].rstrip())


# Prints the char frequency in a nice table using tabulate. Converting the
# solo values into lists was a must
# There's an "update" method that I should use here
def problem_31(path_to_file):
    total_count = counter()
    with open(path_to_file, 'r') as f:
        for line in f:
            total_count += counter(line.rstrip())
        print tabulate({k: [v] for (k, v) in dict(total_count).items()}, headers='keys')


def problem_32(string, word_interval=0, icao_interval=0):
    engine = pyttsx.init('sapi5')
    d = {'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo', 'f': 'foxtrot',
         'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett', 'k': 'kilo', 'l': 'lima',
         'm': 'mike', 'n': 'november', 'o': 'oscar', 'p': 'papa', 'q': 'quebec', 'r': 'romeo',
         's': 'sierra', 't': 'tango', 'u': 'uniform', 'v': 'victor', 'w': 'whiskey',
         'x': 'x-ray', 'y': 'yankee', 'z': 'zulu', ' ': ' '}
    engine.say(string)
    engine.runAndWait()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate + 30)
    for word in string:
        for letter in word:
            time.sleep(icao_interval)
            engine.say(d[letter])
            engine.runAndWait()


def problem_33(path_to_file):  # Returns unique words in a text
    with open(path_to_file) as f:
        word_counter = dict(counter(f))
        return [k.rstrip() for k, v in word_counter.items() if v == 1]


def problem_34(path_to_file, path_to_written_file):  # Enumerates a text
    with open(path_to_file, 'r') as f:
        with open(path_to_written_file, 'w') as f2:
            for i, line in enumerate(f):
                f2.write('{}. {}'.format(i + 1, line))


def problem_35(path_to_file):  # Returns the avg lengh of the words
    with open(path_to_file) as f:
        total_words = counter(f)
    with open(path_to_file) as f:
        total_chars = counter(letter for line in f
                              for letter in line.lower()
                              if letter in ascii_lowercase)
    return float(sum(total_chars.values())) / float(sum(total_words.values()))


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
    print problem_12([2, 3, 6])
    print problem_13([1, 3, 4, 13943, 6, 7])
    print problem_14(['aaaa', 'ask', 'akshg', '12345j'])
    print problem_15(['aaa', 'aa', '12354567'])
    print problem_16(['123', '12345', '12'], 2)
    print 'Problem 17, ', problem_17('Was it a rat I saw')
    print problem_18('The quick brown fox jumps over the lazy dog')
    problem_19()
    print problem_20('Happy merry christmas')
    print problem_21('aasssasdasdsasdasdasdggbcxvc')
    print problem_22('Pnrfne pvcure? V zhpu cersre Pnrfne fnynq', 'decode')
    print problem_23('Yhis   is.ery funny  and    cool.Indeed!')  # INCORRECT
    print problem_24('try')
    print problem_25('see')
    print problem_26([1, 3, 5, 56, 345, 2])
    print problem_27(['aaa', 'bbbbbb', 'cj'])
    print problem_28(['aaa', 'bb', 'asdasdasd'], 2)
    problem_29('E:\Code\outros\problem_29.txt')
    print problem_30("e:\code\outros\problem_30.txt")
    print problem_31("e:\code\outros\problem_30.txt")
    #problem_32('ball park', 1, 2)
    pprint(problem_33('E:\code\outros\problem_30.txt'))
    problem_34(
        'E:\code\outros\problem_30.txt', "E:\code\outros\problem_34.txt")
    print problem_35('E:\code\outros\problem_30.txt')


test()
