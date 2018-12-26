lower_line = '4:heLLolkajs hellooo'
line = '4:hELLOlkajs hellooo'
char = 'hello'
def color(char, lower_line, line):
    final_string = ''
    while char in lower_line:
        length = lower_line.index(char[0]) + len(char)
        final_string += line[:lower_line.index(char[0]):]
        final_string += '\033[30;43m' + line[lower_line.index(char[0]):length:] + '\033[0m'
        line = line[length::]
        lower_line = lower_line[length::]
        color(char, lower_line, line)
    final_string += line
    return final_string
print(color(char, lower_line, line))
