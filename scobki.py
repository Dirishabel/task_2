def response_collector(isCorrect: bool, not_close: list, error_char: list):
    if isCorrect:
        print(isCorrect, None, None, ret_num)
    else:
        print(isCorrect, tuple(not_close), tuple(error_char), ret_num)
def isCorrectBrackets(string: str, brackets: list):
    temp_row = []
    brackets_list = []
    for i in brackets:
        if i == '{':
            brackets_list.append('{')
            brackets_list.append('}')
        if i == '[':
            brackets_list.append('[')
            brackets_list.append(']')
        if i == '(':
            brackets_list.append('(')
            brackets_list.append(')')
        if i == '<':
            brackets_list.append('<')
            brackets_list.append('>')
    iteration=0
    temp_not_close = ()
    temp_error_char = ()
    for char in range(len(string)):
        if string[char] in brackets_list:
            if string[char] in brackets:
                temp_row.append((string[char], char))
            else:
                if not temp_row:
                    return response_collector(False , [string[char], char], [string[char], char])
                temp_char = temp_row.pop()
                for i in range(0,len(brackets_list),2):
                    if temp_char[0] == brackets_list[i] and string[char] != brackets_list[i+1]:
                        temp_not_close = temp_char
                        temp_error_char = (string[char], iteration)
                        return response_collector(False , (string[char], iteration), temp_not_close)
        iteration+=1
        
    return response_collector(len(temp_row) == 0 , [string[char], char], temp_row[-1])

input_string = input()
brackets = input()
correct_string = isCorrectBrackets(input_string, brackets)
