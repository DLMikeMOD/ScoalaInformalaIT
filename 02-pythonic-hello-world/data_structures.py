lista = [8, 3, -66, "string", 2.7, -5]
# print (lista[3])
print (lista[1:]) # arata tot din lsita incepand cu indexul cu care incepi, si poti sa adaugi alt numar dupa : unde sa se opreasca dar exclude ultimul obiect din lista selectat
print (lista[0:5:2]) # daca pui un numar care este peste index arata chair si ultima intrare deci toata lista si inca 2 la sf arata din 2 in 2
print (lista [-1]) # ia ultimul element din lista no matter how big the list is
print (lista [-1: -3: -1]) # asa merge invers in lista intre indexi
print (lista [-1::-1]) # display toata lista dar o ciste invers

lista.append("Demoni")
lista[3] = "sucubby" # face update prin index in lista principala si da diplay mai jos la latest version
print(lista) # print(len(lista)) arata cat de mare e  lista
print(lista.index(-5))
lista.insert(3, "element nou") # adauga un nou element la indexul cutare si le muta pe toate restu la dreapta
lista.pop (3) # sterge din lista de la id-ul selectat
# lista.clear () #sterge tot
# lista.reverse () #face reverse la lista
lista2 = ["1", "3", "6", "8!", "-2"]
lista2.sort() # face sortare cum trebuie
print (lista2)

