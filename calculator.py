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

<<<<<<< HEAD
    if restart == 'Да':
        calculator()
    elif restart == 'Нет':
        print('До встречи, вацок...')
        break
=======
if restart == 'Еще' or 'Ещё':
    calculator()
elif restart == 'Нет':
    print('Ну как знаешь, вацок...')
# Почему то после слова "Нет" программа заново запускается
>>>>>>> 4ee9e21f108d9bbda74ad0126918d1b83a361d18
