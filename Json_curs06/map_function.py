# def adunare(n):
#     return n + n

lista_numere = [1,2,3,4]
lista_numere2 = [5,6,7,8,9]
# rezultat = map(adunare, lista_numere)
# print(list(rezultat))

rezultat = map(lambda n, m: n + m, lista_numere, lista_numere2) #way easyer this way
print(list(rezultat))