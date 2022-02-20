# lista_numere = [1,2,3,4,5,6,7,8,9,10]
#
# def functie_nr_pare(number):
#     if number % 2 ==0:
#         return True
#     return False
#
# iterator_numere_pare = filter(functie_nr_pare, lista_numere)
# print(list(iterator_numere_pare))

# litere = ['a', 'b', 'c', 'd', 'e', 'i', 'j']
#
# def filter_vocale(letter):
#     vocale = ['a', 'e', 'i', 'o', 'u']
#     return True if letter in vocale else False

# x = 1
#
# def f():
#     return x
#
# print(x)
# print(f())

# x = [1,2,'hello', 'world', ['another', 'list']]
# print(len(x[3]))

# a = [1,2,3]
# b = [4,5]
#
# print(a+b*3)

# x = [1,2,3,4]
# print(x[-1:])

# x = [0,1,[2]]
# x[2][0] = 3
# x[2].append(4)
# x[2] = 2
# print(x)


# def exercitiu(i):
#     for i in range(i):
#         return i
#
# x = exercitiu(3)
# print(x)


def funct(*args):
    return 3 + len(args)

print(funct(4,4,4))