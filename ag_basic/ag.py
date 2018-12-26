import sys
import re


def list_lines(file):
    f = open(file, 'r')
    all = f.read()
    f.close()
    lines = all.split('\n')
    return lines


"""Return list of lines in file"""


def print_character(char, lower_lines, lines, case):
    for i in range(len(lower_lines)):
        if lower_lines[i].find(char) != -1:
            print('\033[1;33m' + str(i+1) + '\033[0m'  + ':', end='')
            print(color(char, lower_lines[i], lines[i], case))


"""Print the colored strings have character in file"""


def color(char, lower_line, line, case):
    final_string = ''
    start = '\033[30;43m'
    end = '\033[0m'
    if case == 'insensitive':
        while char in lower_line:
            length = lower_line.index(char[0]) + len(char)
            final_string += line[:lower_line.index(char[0]):]
            final_string += start + line[lower_line.index(char[0]):length:] + end
            line = line[length::]
            lower_line = lower_line[length::]
            color(char, lower_line, line, case)
        final_string += line
    else:
        colored = start + char + end
        final_string = re.sub(char, colored, line, 0, 0)
    return final_string


"""Return insensitive colored string"""


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
        char = char.lower()
        print_character(char, lower_lines, lines, case)
        quit()
    lower_lines = lines
    print_character(char, lower_lines, lines, case)


ag()
