print ("Numele meu este Mike")
# comments
print (1, type(-1)) #tipul int (intreg)
print (1.1, type(1.1)) # tipul float  (rational.zecimal)
print (1j, type(1j)) # tipul complex
# you can also print all the reuslts type (print complex, float,etc)
print (5//2) #catul
print (5%2) #restul (modulo)

print (5 == 2) #boolean True sau False ("==" "!=" ">" "<" ">=")

print (5 > 2 or 3 > 1) #merge sa adaugi and si or
print (not(5>2 and 3>1)) #operator de negare
print (7 is 7) #afirma
print (7 is not 7) #afirma

nicu_varuieste, nicusor_varuieste = 0, 69
# nicu_varuieste = None # none este null in zona de memorie nu se poate sa aduni asta cu nimic
nicu = 2
nicu += 3 # in exemplul asta scurtezi (nicu = nicu + 1) merge scurtat codul asa si sa schimbi inainte de = orice functie matematica suportata
print (nicu)
print (nicu_varuieste, nicusor_varuieste)

ana = "Ana 'are' \n Dildo-uri MAAARI" # merge si reverse intre ghilimele sa dai print in mijloc sau forma mai complexa \'are\'
# /n e new line un fel de <br>
ana = """Ana 'are' 
Dildouri mari"""
# in exemplul cu 3 ghilimele pune texutul unde il pui tu in cod cu enter autoformat nice
print (ana)

nume = "Seitan"
prenume = "Milostivul"
varsta = 420
prezentare = "Numele Lordului tau este {1} si prenumele este {0}".format(nume, prenume) # util sa dai display la date si sa rulezi inline si poti sa le schimbi direct din acolade cu 0,1,etc, si cand incepi sa scrii indexul in acolade trebui sa le pui peste toate
print (prezentare)
prezentare = f"Numele Lordului tau este {nume}, prenumele este {prenume} iar varsta lui este de {varsta} de ani." # exact ca mai sus doar ca nu mai pui format la sfarsit si e mai scurta I like this one so far merge blanao
print (prezentare)

calcul = nume + prenume
print (calcul)

