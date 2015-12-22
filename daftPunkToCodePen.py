import itertools


song = '''Work it, make it, do it, makes us
Harder, better, faster, stronger

More than, hour, our, never
Ever, after, work is, over

Work it, make it, do it, makes us
Harder, better, faster, stronger

Work it harder
Make it better
Do it faster
Makes us stronger

More than ever
Hour after our
Work is never over

Work it harder
Make it better
Do it faster
Makes us stronger

More than ever
Hour after our
Work is never over

Work it harder make it better
Do it faster makes us stronger
More than ever hour after
Our work is never over

Work it harder make it better
Do it faster makes us stronger
More than ever hour after
Our work is never over

Work it harder make it better
Do it faster makes us stronger
More than ever hour after
Our work is never over

Work it harder make it better
Do it faster makes us stronger
More than ever hour after
Our work is never over

Work it harder make it better
Do it faster makes us stronger
More than ever hour after
Our work is never over

Work it harder make it better
Do it faster makes us stronger
More than ever hour after
Our work is never over

Work it harder make it better
Do it faster makes us stronger
More than ever hour after
Our work is never over

Work it harder make it better
Do it faster makes us stronger
More than ever hour after
Our work is never over

Work it harder make it better
Do it faster makes us stronger
More than ever hour after
Our work is never over

Work it harder
Do it faster
More than ever
Our work is never over

Work it harder make it better
Do it faster makes us stronger
More than ever hour after
Our work is never over
'''


word_dict = {"Work": 'Q', "Make": 'W', "Do": 'E', 'Makes': 'R', 'Harder': 'A', 'Better': 'S', 'Faster': 'D', 'Faster,': 'D', 'Stronger':
             'F', "More": 'U', 'Hour': 'I', 'Our': 'O',
             'Never': 'P', 'Ever': 'J', 'After': 'K', 'Is': 'L', 'Over': ';'}


def getRelevantWords(song, translate_dic=None):
    translated = []
    for word in song.split():
        word = word.split(',')[0]
        word = word.capitalize()
        # print word
        if word in word_dict.keys():
            translated.append(('{}'.format(translate_dic[word])))
            # print '{}:{}'.format(translate_dic[word], word)
    return translated


def countWords(song, word_dict):
    words_n = []
    for line in song.split('\n'):
        valid_words = []
        for word in line.split():
            word = word.split(',')[0]
            word = word.capitalize()
            # print word
            if word in word_dict.keys():
                valid_words.append(word)
        words_n.append(len(valid_words))
    return words_n


def printing(text, words_per_line):
    for limit in words_per_line:
        if not text:
            break
        line = text[:limit]
        text = text[limit:]
        print(' '.join(line))

def printing2(toPrint, words_per_line):
    for n_words in words_per_line:
        line = ' '.join([toPrint.pop(0) for _ in range(n_words)])
        print(line + '\n')


def main():
    inputList = getRelevantWords(song, word_dict)
    l = ['' if item == 'Q' and item2 == "L" else item for item,
         item2 in zip(inputList, inputList[1:])]
    printing2(l, countWords(song, word_dict))

main()