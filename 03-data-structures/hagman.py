# rules
# daca primul caracter si ultimul se repetau in cuvant, caracterul trebui sa fie afisat iar restul caracatrerelo sunt ascunse
# 7 sanse de a ghici cuvantul, aftrer you fail 7 times you die
# word = o _ o _ _ _ 0 _ e e
# litera_cuvant = input("Alege o litera") # iti merge input de user chair si in consola
# print

word = 'onomataopee'
lista_cuvant= []
for iterator in word:
    lista_cuvant.append('_')
    if iterator == word[0] or iterator == word[-1]:
        lista_cuvant[-1] = iterator
print(' '.join(lista_cuvant))
numar_incercari = 1
lista_litere_incercate = set()
while numar_incercari <= 7:
    litera = input("Alege o litera: ").lower()
    if litera in word.lower():
        for index, valoare in enumerate(word):
            if valoare.lower() == litera:
                lista_cuvant[index] = litera
    else:
        if litera.lower() not in list(lista_litere_incercate):
            numar_incercari += 1
        lista_litere_incercate.add(litera.lower())
        print (f'Litenra nu exista, deja ai incercat urmatorele litere {",".join(lista_litere_incercate)}')
        print (f"Mai ai {7 - numar_incercari} incercari")

    if 9 - int(numar_incercari) == 0:
        print(f"YOU DIED. Cuvantul era {word}")
    elif ''.join(lista_cuvant) == word:
        print("Ai Castigat!")
        break
    else:
        print(''.join(lista_cuvant))

# must be very very carefull with god damn indentation

