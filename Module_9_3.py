first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = ((len(x) - len(y)) for x,y in zip(first, second) if len(x) != len(y))
second_result = (True if len(x)==len(y) else False for x in first for y in second)



print(list(first_result))
print(list(second_result))