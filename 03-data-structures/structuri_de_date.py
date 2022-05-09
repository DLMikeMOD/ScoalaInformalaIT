#tupluri
lista = [1, 2, 3, 1, 'a']
lista_1 = ['a', 'b', 'c']
lista_total = lista + lista_1
print(lista_total)
tuplu =(1, 2 ,3 ,1, 'a')
tuplu_1 =(1, 2 ,3 , 'b')
tuplu_total = tuplu + tuplu_1
print(tuplu_total)
tuplu_nou = ('1',) # asa se foloseste tuplu de un singur element si sa se termeni in virgula pe ultimul element
print(type(tuplu_nou))


dictionar = {"key1": '1', 1: '1', 'lista': [1, 2, 3]} # pot sa am orice in dictionar
print (dictionar ['key1'])   # print (dictionar.get ['key2']) pot sa imi zica ca nu exista
dictionar ['key2'] = 69
dictionar ['key1'] = 2 # face update cumva legacy
dictionar.update({"key1" : 3}) #face update mai nou, also ultima voloare de update se ia in ordinea in care s-au scris
print (dictionar.keys())
print (dictionar.values())
print (dictionar.items())


setul = {1, 2, 3 } # asta e un set de date
print(setul) # asa afiseaza elemenetele unice
print (lista_total)
print (set(lista_total)) # setul de obicei ordoneaza