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

while True:
    restart = input('Если хочеть еще че нибудь намутить напиши "Да", если не хочешь "Нет": ')

    if restart == 'Да':
        calculator()
    elif restart == 'Нет':
        print('Ну как знаешь, вацок...')
