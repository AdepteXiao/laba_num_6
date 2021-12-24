"""
КИ21 - 17/1b Демёхина Арина Руслановна
ОП Лабораторная №4
Вариант 22
"""


from sys import exit


def printable_expression():
    """Вывод на экран введенного выражения"""
    if expression == '':
        print('Вы ещё не ввели никакое выражение')
    else:
        return ''.join(expression.pop())


def polska():
    """Преобразование в обратную польскую запись вводимого числа"""
    global expression, checkout, result
    result = []
    checkout = ['!']
    checklist = 'abcdefghijklmnopqrstuvwxyz1234567890/+-*()'
    while not set(expression := list(input('Введите выражение без пробелов:\n'))).issubset(checklist):
        print('Выражение введено неверно, попробуйте снова')
    op = 0
    cl = 0
    for x in expression:
        if x == ')':
            op += 1
        elif x == '(':
            cl += 1
    if op == cl:
        expression.append('!')
        for i in expression:
            strelka = 0
            while strelka == 0:
                if i.isdigit() or i.isalpha():
                    result.append(i)
                    strelka += 1
                else:
                    func = variations[str(cipher[checkout[-1]])][int(cipher[i])]
                    if func.__name__ == 'one':
                        func(i)
                        strelka += 1
                    elif func.__name__ == 'two':
                        func()
                    else:
                        func()
                        strelka += 1
    else:
        print('Проверьте правильность написания скобок')
        polska()


def one(i):
    checkout.append(i)


def two():
    result.append(checkout[-1])
    checkout.pop()


def three():
    checkout.pop()


def four():
    print(f"Переработанный результат:\n{''.join(result)}")


def five():
    print('Ошибка в написании формулы, попробуйте снова')


result = []
checkout = ['!']
expression = []
cipher = {'!': 0,
          '+': 1,
          '-': 2,
          '*': 3,
          '/': 4,
          '(': 5,
          ')': 6}
variations = {'0': (four, one, one, one, one, one, five),
              '1': (two, two, two, one, one, one, two),
              '2': (two, two, two, one, one, one, two),
              '3': (two, two, two, two, two, one, two),
              '4': (two, two, two, two, two, one, two),
              '5': (five, one, one, one, one, one, three)}
menu = {
    '1': ('Вывести введенное выражение', printable_expression),
    '2': ('Преобразовать в обратную польскую запись', polska),
    '3': ('Выход из программы', exit)
}
while True:
    printable_menu = ''
    for key3, val3 in menu.items():
        printable_menu += f'{key3} - {val3[0]}\n'
    opt = input(f"Выберете опцию:\n{printable_menu}\n")
    if opt in menu.keys():
        print(menu[opt][1]())
    else:
        print('Такого варианта выбора нет\n')
