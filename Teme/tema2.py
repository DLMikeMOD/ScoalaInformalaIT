def add_numbers(*args, **kwargs): #most usefull trick i`ve learned this week
    s = 0
    for arg in args:
        try:
            s += int(arg)
        except (ValueError, TypeError):
            print(f'{arg} invalid!')

    for key, value in kwargs.items():
        try:
            s += int(value)
        except (ValueError, TypeError):
            print(f'{key}:{value} invalid!')

    print(f'sum={s}')
    print()

add_numbers(1, 2, 3, 125, 'a')

def no_result():
    return 0
print(no_result())

add_numbers(
    'x', 'abc', [(1, 2), (3, 4), 'asad'], 5.12, do_something=False, change_something=12
)

def o_functie():
    un_nr = input('Da si tu un numar sau ceva de la tastura BUOI! : ')
    is_int = True

    for char in un_nr:
        if not (char >= '0' and char <= '9'):
            is_int = False
    if is_int:
        print(f"No acilea e numarul tau:  {un_nr}" )
    else:
        print(f"Ehh EEh EEEEE nu dasi un numar asa ca nu pot sa iti zic decat: {0} ")
o_functie()
