def print_string(s):
    for i, x in enumerate(s,start=1):
        print(f'{str(i).zfill(2)}', f'"{x}"', '| ', end='')
        if i != 0 and i % 15 == 0:
            print('')


def get_user_input():
    initial_string = "The Inquisitor must meet Varric on top of the Skyhold`s battlements to be introduced."
    while True:
        user_input = input(f"Vrei sa modifici propozitia {initial_string} (yes/no)?")
        if user_input == "yes":
            print_string(initial_string)
            starting = int(input("Introdu indexul de inceput: "))
            if starting < 1:
                print("Indexul de inceput trebuie sa fie 1")
                continue
            ending = int(input("Introdu indexul de sfarsit: "))
            new_text = input("Introdu cuvantul nou: ")
            # patches.append([starting,ending,new_text])
            value = initial_string[starting - 1 : ending]
            initial_string = initial_string.replace(value, new_text)
        elif user_input == "no":
            print_string(initial_string)
            break

get_user_input()
