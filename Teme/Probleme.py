# 1. Scrie un program care sa calculeze suma dintre trei numere.
# Daca valorile sunt egale, returnati de trei ori suma acestora.

# def suma3():
#     a = int(input('A= '))
#     b = int(input('B= '))
#     c = int(input('C= '))
#
#     if a == b == c:
#         return 3 * (a + b + c)
#     else:
#         return a + b + c
#
#
# print(suma3())

#
# 2. Scrie un program care sa elimine si sa printeze numerele din 3 in 3 pana cand lista devine goala.
#
# lista =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
#x = list(range(1, 14))
#
# print(x)
#
# while len(x) > 0:
#     to_remove = []
#     for i in range(2, len(x), 3):
#         elem = x[i]
#         to_remove.append(elem)
#
#     print(to_remove)
#     for elem in to_remove:
#         x.remove(elem)
#
#     if not to_remove:
#         x = []
#
#     print(x)
#     print('-------')




# Scrie un program care sa afiseze toate combinarile de 2 litere dintre valorile dictionarului de mai jos:

# dictionar = {"1": "abc",
#              "2": "s",
#              "3": "o",
#              "4": "n",
#              "5": "lm",
#              "6": "jk",
#              "7": "gi",
#              "8": "def",
#              "9": "abc"}
#

# def sum3(a, b, c):
#     sum = 0
#     if a == b == c:
#         sum = a + b + c
#         return f"{3 * sum} sau {sum} {sum} {sum}"
#     return a + b + c
#
# num1 = int(input("Introduceti primul numar: "))
# num2 = int(input("Introduceti al doilea numar: "))
# num3 = int(input("Introduceti al treilea  numar: "))
#
# print(sum3(num1,num2,num3))

#
# dictionar = {"1": "abc","2": "s","3": "o","4": "n","5": "lm","6": "jk","7": "gi","8": "def","9": "abc"}


# i = 1
# while  True:
#     if i%3  == 0:
#         break
#     print(i)
#     i += 2

#
# 1. Se dă un şir cu cel mult 10 caractere. Să se determine câte vocale conţine. (1 punct)


# vocale = {'a','e','i','o','u'}
#
# numero = "ia gaseste"
#
# for i in numero:
#   if i in vocale:
#     print(f"Toate vocalele gasite in propozitia ta sunt {i}")

#
# 2. Sa se scrie un program care sa calculeze impartirea dintre trei numere.
# Daca valorile sunt egale, returnati de trei ori rezultatul.
# Impartirea la 0 va duce la rezultatul 0. (1 punct)

# def suma3():
#     a = int(input('First Numbah = '))
#     b = int(input('Second Numero= '))
#     c = int(input('Third Numar= '))
#
#     if b == 0 or c == 0 :
#         return 0
#
#     if a == b == c:
#         return 3 * (a / b / c)
#     else:
#         return a / b / c
#
# print(f"All dem number added times 3 is bout: {suma3()}")



# 1. Se da sirul de numere n care contine [1, 2, 3, 4, 5, 6, 7].
# Sa se insereze in acest sir dupa fiecare element par, dublul acestuia (2 puncte)

# Try 1 simple but not complete
# n= [1, 2, 3, 4, 5, 6, 7]
#
# def convert(n):
#     return tuple(n)
# print(convert(n))
#
# for numero in convert(n):
#
#     if numero % 2 == 0:
#         print(numero, numero*numero)
#
#
#
n= [1, 2, 3, 4, 5, 6, 7]

otherlist = []
for i in n:
    # print(i)
    otherlist.append(i)
    if i % 2 == 0:
        otherlist.append(i * i)

print(otherlist)

# def convert(n):
#     return tuple(n)
# print(convert(n))

# for numero in convert(n):
#
#     if numero % 2 == 0:
#         print(numero, numero*numero)


# n= [1, 2, 3, 4, 5, 6, 7]
#
# def convert(n):
#     return tuple(n)
# print(convert(n))
#
# for numero in convert(n):
#
#     if numero % 2 == 0:
#         print(numero, numero*numero)
#
#         otherlist = []
#         for i in n:
#             print(i)
#             otherlist.append(i)
#             if i % 2 == 0:
#                 otherlist.append(i*i)
#
#         print(otherlist)

#create a tuple
# tuplex = (1, 2, 3, 4, 5, 6, 7)
# print(tuplex)
#tuples are immutable, so you can not add new elements
#using merge of tuples with the + operator you can add an element and it will create a new tuple
# tuplex = tuplex + (9,)
# print(tuplex)
#adding items in a specific index
# tuplex = tuplex[:2] + (4) + tuplex[:5]
# print(tuplex)

#
# def linear_list (n):
#     x = []
#     for y in range (1, n+1):
#         x.append (y)
#     return x


# n = int (input ("Enter the lenght of the list: "))

# alist = linear_list (n)
#
# for i in alist:
#     print (i)
#     if i % 2 == 0:
#         alist.append(0)
#
# print (alist)
