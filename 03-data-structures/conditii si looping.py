# daca conditie :
    #print ('adevarat)
#daca alta conditie:
    #print('nici aceasta nu e adevarata'
#altfel:
    # print (afisez doar daca "conditie" si "alta conditie" nu sunt adevarate)

# also functia "if" este obligatoriu cand construiesti o functie conditionata

# varia_1 = 5
#
# if varia_1 < 6:
#     print("Data 1")
# elif varia_1 < 10:
#     print("Data 2")
# else:
#     print( "Data 3")
# print ('a iesit')
#asa se scrie functia conditionaal veche cica



# varia_1 = 7
# mesaj = "Set data 3"
#
# if varia_1 < 6:
#     mesaj= "Set data 1"
# elif varia_1 < 10:
#     mesaj= "Set data 2"
#     print(mesaj)
#     print("A iesit")
# asta e o metoda sa scrii fara functia "else" codul
# var = 1
# while var < 10:
#     var += 1 #inseamna var = var + 1, also depinde unde pui varul deasupra de print sau sub print
#     print("bloc de date", var)
#     # break # asta opresete fortat un while care nu are alta conditie
# bulinele pacii ajuta mult si la fel si butopnul Step Over

#
# string = "Anaa are de toate"
# for i in string:
#     print(i)

# lista = [1, 2, 3 , 'a']
# string = "Anaa are de toate"
# # for i , v in enumerate(lista):
# #     print(i, '=>', v)
# for variabila_temporara in range(0, len(lista)):
#     print(lista[variabila_temporara])
#     print (variabila_temporara, '>>')
#

dictionar = {1: 'unu', 2: 'doi', 3: 'trei'}
# for item, value in dictionar.items():
#     print(item, value)
for item in dictionar.keys():
    print(item, dictionar.get(item)) # same thing
