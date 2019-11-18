# l = [1, 2, 3, 'hello', ['test', 10], 'world', True]
# l2 = list('hello')
# l3 = list((1, 2, 3))
#
# l4 = [i for i in 'hello']
# l5 = [i for i in 'hello world' if i not in ['a', 'e', 'i', 'o', 'u', ' ']]
#
#
# print(l, l2, l3, l4, l5, sep='\n')


# l6 = list(range(0, 11))
# print(l6)

# for i in range(1, 3):
#     print(f'Внешний цикл №{i}')
#     for j in range(1, 3):
#         print(f'\tВнутренний цикл №{j}')


# for i in range(1, 10):
#     print(f'{i} * {i} =', i * i)
#     for j in range(1, 10):
#         print(f'{j} * {j} =', j * j)
#     else:
#         print(end='\n')


# ТАБЛИЦА УМНОЖЕНИЯ
# print('Таблица умножения')
#
# for i in range(1, 10):
#     for k in range(2, 10):
#         print(f'{i} * {k} = {i * k}\t', end=' ')
#     print(' ')
# else:
#     print('Well done')
#
#


# l = [1, 2, 3, 'hello', ['test', 10], 'world', True]

# print(l[4][1])
# l[2] = 'world'

# l[:2] = [10, 15]

# l.append('new')
# l.extend([5, 7])
# l2 = ['hi', 19]
# l += l2
# l.insert(1, 'test')
# l.remove('world')
# el = l.pop()

# l.sort()
# l3 = ['hello', 'hi', 'david', 'test']
# l3.sort()


l = [1, 2, 3, 'world', 'hello', ['test', 10], 'world', True]

while 'world' in l:
    l.remove('world')


print(l)




