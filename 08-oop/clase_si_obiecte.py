# class FirstClass:
#     pass
#
# my_first_object = FirstClass()

#
# class Dog:
#     paw_number = 4  # atribut al unei clase
#
#     def __init__(self, name, age=69):   # constructori is astia
#         self.nume = name
#         self.varsta = age
#
#     def __str__(self):   #si initiatori si ajuta sa creezi obiecte cu date diferite
#         return f"{self.nume} cu varsta {self.varsta}"
#
#
#     def change_name(self, name):  # asta e metoda clasei
#         self.nume = name
#         return 'Muie Rusia'

# print(Dog.paw_number)

# my_dog = Dog("Satana")  #proprietate

# print(my_dog.change_name('Flischi'))
# print(my_dog)
# print(my_dog.varsta)

class Calculici:

    def __init__(self, op1, op2, operation):
        self.operator1 = op1
        self.operator2 = op2
        self.operatie = operation

    def adunare(self):
        return self.operator1 + self.operator2

    def __str__(self):
        if self.operatie == "+":
            return f"{self.adunare()}"

obiect1 = Calculici(1, 2, '+')
print(obiect1)