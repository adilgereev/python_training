print('Приветствую на своем супер-мощном калькуляторе!')

def calculator():

    while True:
        x1 = int(input('Вацок, введи первое число: '))
        print('Красиго!')
        operator = input('А теперь введи один из знаков операции (+, -, *, /): ')
        x2 = int(input('И второе число для операции: '))

        if operator == '+':
            print('Шикардос!')
            print(f'{x1} + {x2} = {x1 + x2}')
            break
        elif operator == '-':
            print('Четко!')
            print(f'{x1} - {x2} = {x1 - x2}')
            break
        elif operator == '*':
            print('Мощно!')
            print(f'{x1} * {x2} = {x1 * x2}')
            break
        elif operator == '/':
            print('Зачет!...')
            print(f'{x1} / {x2} = {x1 / x2}')
            break
        else:
            print('Будь по проще, уци! Вводи символы соответствующие функционалу калькулятора!')


calculator()

while True:
    restart = input('Если хочешь еще раз провести какую нибудь опасную операцию введи "Да", если не хочешь введи "Нет": ')

    if restart == 'Да':
        calculator()
    elif restart == 'Нет':
        print('До встречи, вацок...')
        break
# Почему то после слова "Нет" программа заново запускается
