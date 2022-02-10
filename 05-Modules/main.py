# print() #str
# input() #str
# "".format # str

# def functie2():
#     my_function()
#
# def my_function ():
#     return ""  #poti sa nu ai nimic in return dar tre sa ai return "" sau '' altfel in exewmplul asta o sa fie none by default
#
#
# print (my_function())


# def mesaj ():
#     print("Enter a value")
# mesaj()


# def cartof(name: str) -> str:
#     print("Hello", name)
#     return name
#
# name = input("Eu sunt un: ")
# cartof(name)

# def functia (a: str, b: str, c: str) -> (str, str, str):
#     return a, b, c
#
# # print(functia (a='1', c='2', b='3'))
# # print(functia ('1', '3', '2')) # sau asa
# # print(functia('1', c='2', b='3')) # merge si asa chiar
# # print(functia('3', a='1', c='2')) # ASA NU E BINE ca rescrii a
# print(functia('1', '3', c='2'))


# def alta_functie():
#     pass
#
# a = alta_functie()
# print(a)
# b=None
# print(type(b))


# def functione(n):
#     if n % 2 == 0:
#         return True
#     return False
#
# print(functione(4))
# nr = input("Introdu un numero: ")
# if functione(int(nr)) is True:
#     print("Numarul este divizibil")
# elif functione(int(nr)) is False:
#     print("Numarul nu este divizibil")


# def inca_ofunctie(var1):
#     global var
#     var = var1
#     return f"Cunosti aceasta variabila: {var}"
#
#
#
# print(inca_ofunctie(3))
# var=1 #conteaza totusi si unde pui valorile fixe
# print(var)


# lista = [1, 2, 3 , [4, 5, [6, 7]]]
#
# print(lista[3][2][0]) # asa afisezi elementul 6 care e intr-o lista din alta lista in alta lista
#

# try:
#     #bloc de expresii
# except:
#     # daca apare ceva exceptie si vrem sa afisam ceva

try:
    valoare = int(input("Prima cifra din cnp: "))
    # impartire = 1/valoare
    lista = [1]
    # lista.append("2")
    # valoare = lista[0.5]
    print("Trial") #daca pun litera nu mai ajunge aici
except (TypeError, ZeroDivisionError, Exception, ValueError, AttributeError):
    print("Ceva eroare")
else:
    print("nu exista exceptie")
finally:
    print("se exectua oricum")
print("am iesit din try-except")
# except AttributeError:
#     print("eroare la atribuire")
# except ValueError:
#     print("Ai introdus o litera in loc de cifra")
# except Exception as e:  # in cazul asta Exception mai puternic decat ZeroDivision
#     print("Exceptie la impartire", e)
# except ZeroDivisionError:
#     print("Eroare la impartire")
