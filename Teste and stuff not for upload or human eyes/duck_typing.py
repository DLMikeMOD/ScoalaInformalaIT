class Animal:
    def __init__(self, name):
        self.name = name


class Duck(Animal):
    def quack(self):
        return 'Quack!'


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        return 'Bark!'

    def quack(self):
        return 'Quack!'


duck = Duck('Aris')
dog = Dog('Beam')


a_list = ['a', 123, 3.14, duck, dog]


for elem in a_list:
    print(elem)
    if getattr(elem, 'quack', None):
        print(elem.quack())

    if getattr(elem, 'bark', None):
        print(elem.bark())
