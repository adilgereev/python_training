# t1 = (1, 2, 3)
# print(t1)

# t1 = (10, 11, [1, 2, 3], [4, 5, 6], ['hellow', "world"])
# print(t1)
# t1[4][0] = 'new'
# print(t1)
# t1[4].append('hello')
# print(t1)

# x = 1
# y = 2
#
# print(x, y)
# x, y = y, x
# print(x, y)

"""
Дан список words. Составьте из него список слов-палиндромов. Попробуйте это сделать двумя способами: произвольное решение и решение в одну строчку кода.
Дан список my_str со строками, часть из которых являются палиндромами. Составьте новый список строк-палиндромов.
"""

# Задача №1
# words = ['мадам', 'топот', 'test', 'madam', 'word']
# palindromes = []
# for word in words:
#     if word == word[::-1]:
#         palindromes.append(word)
#
# print(palindromes)
#
# palindromes = [word for word in words if word == word[::-1]]
# print(palindromes)
# задания решены с помощью тренера.


# my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']
# palindromes = []
# for word in my_str:
#     word_r = word.replace(' ', '').lower()
#     if word_r == word_r[::-1]:
#         palindromes.append(word)
#
# print(palindromes)

l = list(range(1, 10))
l2 = list('hello')

s = '-'.join(map(str, l))
s2 = ','.join(l2)

print(s)
print(s2)