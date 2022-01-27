lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
asc=lista.sort()
asc_ord = f"Lista ordonata ascdent {lista}"
print(asc_ord)

desc = lista [-1::-1]
asc_desc = f"Lista ordonata descdendent {desc}"
print (asc_desc)

list_slice0 = lista [1::2]
lista_slice1 = lista [::2]
even_f = f"Numerele pare din aceasta lista sunt {list_slice0} \nIar numerele impare sunt {lista_slice1}"
print (even_f)

multiply = lista [2:9:3]
mul3 = f"Multipli de 3 din aceasta lista sunt {multiply}"
print (mul3)