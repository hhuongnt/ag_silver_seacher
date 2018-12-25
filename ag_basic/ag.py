import sys


def readfile(file):
    f = open(file, 'r')
    return f.read()


"""Read file"""


def list_lines(file):
    f = open(file, 'r')
    all = f.read()
    f.close()
    lines = all.split('\n')
    return lines


"""Return list of lines in file"""


def find_character(file, char, lines):
    words_have_char = []
    for i in lines:
        list_char = []
        list_char = i.split(' ')
        for j in list_char:
            if j.find(char) != -1:
                words_have_char.append(j)
    return words_have_char


"""Return list of the words have character in file"""


def ag():
    list_cmd = sys.argv
    for i in list_cmd:
        if i == '--case-sensitive':
            list_cmd.remove(i)
            case = 'sensitive'
        else:
            case = 'insensitive'
    char = list_cmd[1]
    file = list_cmd[2]
    lines = list_lines(file)
    if case == 'insensitive':
        lower_lines = []
        for i in lines:
            lower_lines.append(i.lower())
        words_have_char = find_character(file, char, lower_lines)
        print (words_have_char)
        quit()
    words_have_char = find_character(file, char, lines)
    print (words_have_char)

ag()
