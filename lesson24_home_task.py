"""
Создайте игру "Угадай число". В коде программы в переменную запишите любое число от 1 до 100
(в следующих уроках мы узнаем, как генерировать случайное число), которое и должен угадать игрок.
Далее программа должна спросить у игрока угадать число. Если пользователь не угадал число - программа сообщает,
что загаданное число больше/меньше и предлагает попробовать еще раз,
при этом программа ведет счета кол-ва попыток игрока. Если игрок угадал число,
тогда программа благодарит за игру и сообщает кол-во попыток, за которое было угадано число.
"""

x = 50
s = []

while True:
    y = int(input('Угадай число от 1 до 100: '))
    s.append('+')
    if y == x:
        print('Красавчик, ты угадал число!', 'Количество попыток:', len(s))
        break
    elif y < x:
        print('Введенное число меньше заданного')
    else:
        print('Введенного число больше заданного')

# Решено!
