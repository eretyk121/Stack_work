from Stack_file import Stack

test = '[([])((([[[]]])))]{()}'
test_1 = '(((([{}]))))'
test_2 = '{{[()]}}'
test_3 = '}{}'
test_4 = '{{[(])]}}'
test_5 = '[[{())}]'
test_6 = '[()([{}])]'
def check(text):
    close_dict = {')': '(', ']': '[', '}': '{'}
    my_stack = Stack()
    for i in text:
        if i in '(){}[]':
            if i not in close_dict:
                my_stack.push(i)
            else:
                if close_dict[i] not in my_stack.items:
                    return 'Не сбалансирован. Отсутствие открытой скобки для закрытой'
                    break
                else:
                    if my_stack.size() != 0:
                        my_stack.pop()
                    else:
                        return False
    if my_stack.isEmpty() == False:
        return 'Не сбалансирован'
    else:
        return 'Сбалансирован'

print(check(test_6))

