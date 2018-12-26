import sys
import re


def ag_basic():
    input = sys.argv[1:]
    options = set()
    for element in input:
        if element[:2] == '--':
            options.add(element)
            input.remove(element)

    with open(input[1], 'r') as file:
        lines = []
        for line in file:
            lines.append(line)

    match = []
    count = 0
    for line in lines:
        count += 1
        if '--case-sensitive' in options:
            if input[0] in line:
                match.append('\033[1;33m' + str(count) + '\033[0m' +
                             ':' + line)
            pat = '(' + input[0] + ')'
        else:
            if input[0] in line.lower():
                match.append('\033[1;33m' + str(count) + '\033[0m' +
                             ':' + line)
            pat = '(?i)(' + input[0] + ')'

    for line in match:
        line = re.sub(pat, r'\033[30;43m\1\033[0m', line)
        print(line, end='')


ag_basic()

