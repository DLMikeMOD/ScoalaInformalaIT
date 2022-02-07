# Tipuri de functii
# print ("text")
# format ()
# meh= input("scrie ceva bossule")

# def o_functie_oarecare(param_1):
#     pass

def suma (a: int, b:int, c:int=3) -> (int, int): #deci nu ai cum sa pui parametru defaul la b si sa nu continie pana la sf
    # also poti sa pui si default sa setezi parametru un anumit tip de date
    # also semnul asta -> in cazul de mai sus e paramtrul de iesire ca sa stie functia ce tipuri de date default o sa faca in returnul de mai jos
    """

    :param a: paramentru a
    :param b: parameantru b
    :param c: paramentru c
    :return: adunare
    """
    # 3 ghilimele si enter face docimentatie automata subb paramentrui definiti
    return a + b + c, a - b - c # cu retunr de fapt dai rezultat la functie

variabila_1 = 1
variabila_2 = 2
sum, dif = suma(a=variabila_1, b=variabila_2, c=0) # cu sau fara a sau b = cu varibilele, also daca nu definesti paramtrul la care se ataseaza valoarea (a= sau b =) ordinea este neaparata sa le ai peste tot, si poti sa suprascrii valoarea inline daca nu vrei sa o folsoestui de exemplu la c redeclaram valaoread in 0 din 3
print(sum, dif)                                    # also cu ctrl+p poti sa vezi valoarea default a unuei functii
