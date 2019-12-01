def calculator():
    print('Приветствую на своем супер-мощном калькуляторе!')
    x1 = int(input('Вацок, введи первое число: '))
    print('Красиго!')
    operator = input('А теперь введи один из знаков операции (+, -, *, /): ')
    x2 = int(input('И второе число для операции: '))

    if operator == '+':
        print('Шикардос!')
        print(f'{x1} + {x2} = {x1 + x2}')
    elif operator == '-':
        print('Четко!')
        print(f'{x1} - {x2} = {x1 - x2}')
    elif operator == '*':
        print('Мощно!')
        print(f'{x1} * {x2} = {x1 * x2}')
    elif operator == '/':
        print('Зачет!...')
        print(f'{x1} / {x2} = {x1 / x2}')

calculator()

restart = input('Если захочешь еще какую нибудь опасную операцию провернуть, напиши слово "Еще": ')

if restart == 'Еще' or 'Ещё':
    calculator()
elif restart == 'Нет':
    print('Ну как знаешь, вацок...')
# Почему то после слова "Нет" программа заново запускается
