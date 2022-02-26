import json
import pandas as pd


EXIT_KEYWORD = 'exit'


ALL_TASKS_PATH = 'all_tasks.json'
ALL_CATEGORIES = 'all_categories.json'

categories = ['fizic', 'work', 'cooking', 'shopping', 'gaming']


all_tasks = [
    dict(name='T1', deadline='2022.02.03 00:00:00', owner='Mihai', category='work'),
    dict(name='T2', deadline='2022.07.06 00:00:00', owner='Mihai', category='fizic'),
    dict(name='T3', deadline='2022.01.01 00:00:00', owner='Mihai', category='fizic'),
    dict(name='T4', deadline='2022.05.01 00:00:00', owner='Mihai', category='cooking'),
    dict(name='T5', deadline='2022.01.07 00:00:00', owner='Mihai', category='shopping'),
    dict(name='T6', deadline='2022.01.01 00:00:00', owner='Mihai', category='gaming'),
]


def add_task(all_items):
    task_name = input('Nume task: ')

    if task_name in [t['name'] for t in all_tasks]:
        print('Task-ul exista deja!')
        return

    task_date = input('Data: ')
    # TODO: verificare data
    task_owner = input('Persoana responsabila: ')
    category = input('Categorie task: ')

    if category not in categories:
        print(f'Categoria nu exista! Categoriile sunt: {categories}')
        add_category = input(f'Vrei sa adaugi categoria? Yes/No: ')
        if add_category == 'Yes':
            categories.append(category)
        else:
            # this skips to the next iteration
            return

    all_items.append(
        dict(name=task_name, deadline=task_date, owner=task_owner, category=category)
    )


def write_files():
    with open(ALL_TASKS_PATH, 'w') as fw:
        json.dump(all_tasks, fw)
    with open(ALL_CATEGORIES, 'w') as fw:
        json.dump(categories, fw)


def init_dataframes():
    all_tasks_df = pd.read_json(ALL_TASKS_PATH)
    categories_df = pd.read_json(ALL_CATEGORIES)
    return all_tasks_df, categories_df


if __name__ == '__main__':
    print('Hello. Follow instructions or type "exit" to close the program')

    test_mode = input('test mode? yes/no: ')
    if test_mode == 'no':
        while True:
            option = input('Introduceti optiunea: adauga/exit: ')

            if option == 'exit':
                break
            else:
                add_task(all_tasks)

    write_files()
    all_tasks_df, categories_df = init_dataframes()

    while True:
        option = input('Introduceti optiunea: afisare/sortare/filtrare/adauga/sterge: ')

        if option == 'afisare':
            print(all_tasks_df)
        elif option == 'sortare':
            col = input('Coloana: name/deadline/owner/category: ')
            if col not in ('name', 'deadline', 'owner', 'category'):
                print('Invalid column')
                continue

            order = input('Ordine: asc/desc')

            if order not in ('asc', 'desc'):
                print('Invalid order')
                continue

            ascending = True if order == 'asc' else False
            print(
                all_tasks_df.sort_values(
                    by=col, ascending=ascending, key=lambda : col.str.lower()
                )
            )

        elif option == 'filtrare':
            col = input('Coloana: name/deadline/owner/category: ')
            if col not in ('name', 'deadline', 'owner', 'category'):
                print('Invalid column')
                continue

            val = input('Valoare: ')

            print(all_tasks_df[all_tasks_df[col].str.contains(val, case=False)])

        elif option == 'adauga':
            add_task(all_tasks)
            write_files()
            all_tasks_df, categories_df = init_dataframes()

        elif option == 'sterge':
            task_name = input('Numele task-ului de sters: ')
            all_tasks = [t for t in all_tasks if t['name'] != task_name]
            write_files()
            all_tasks_df, categories_df = init_dataframes()
