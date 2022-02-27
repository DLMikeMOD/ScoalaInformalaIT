import json
import pandas as pd
import datetime
from datetime import datetime


EXIT_KEYWORD = 'exit'


ALL_TASKS_PATH = 'all_tasks.json'
ALL_CATEGORIES = 'all_categories.json'

categories = ['fizic', 'work', 'cooking', 'shopping', 'gaming']

#always have a prepopulated list at the start of the program usefull whren in test mode

all_tasks = [
    dict(name='T1', deadline='2022.02.03 12:22:01', owner='Mihai', category='work'),
    dict(name='T2', deadline='2022.07.06 17:21:69', owner='Ion', category='fizic'),
    dict(name='T3', deadline='2022.01.01 19:18:06', owner='Vasile', category='fizic'),
    dict(name='T4', deadline='2022.05.01 10:19:22', owner='Ana', category='cooking'),
    dict(name='T5', deadline='2022.01.07 18:18:29', owner='Ana', category='shopping'),
    dict(name='T6', deadline='2022.01.01 04:20:42', owner='Mihai', category='gaming'),
]

# add items
def add_task(all_items):
    task_name = input('Nume task: ')

    if task_name in [t['name'] for t in all_tasks]:
        print('Task-ul exista deja!')
        return

# date is tricky with json files as I found out and I need additional help from you Alexandra
    task_date = input('Scrie data si ora in formatul asta te rog (aaaa.ll.zz hh:mm): ')

    # the only reason this is commented bellow is because of Json being a prick
    # actual_date = datetime.datetime.strptime(task_date, '%Y.%m.%d %H:%M')
    # as more info is probably needed using either .strptime or .strftime proves to be problematic when working with Json files and inputs from users as well

# moar inputs
    task_owner = input('Persoana responsabila: ')
    category = input('Categorie task: ')

# check the category yonder and try to add it if its not in the main list
    if category not in categories:
        print(f'Categoria nu exista! Categoriile sunt: {categories}')
        add_category = input(f'Vrei sa adaugi categoria? Yes/No: ')
        if add_category == 'Yes' or 'yes':
            categories.append(category)
        else:
            # this skips to the next iteration
            return
# then adds it to the list
    all_items.append(
        dict(name=task_name, deadline=task_date, owner=task_owner, category=category)
    )

# This is the File Writter
def write_files():
    with open(ALL_TASKS_PATH, 'w') as fw:
        json.dump(all_tasks, fw)
    with open(ALL_CATEGORIES, 'w') as fw:
        json.dump(categories, fw)

# extinct animals dataframe rullz
def init_dataframes():
    all_tasks_df = pd.read_json(ALL_TASKS_PATH)
    categories_df = pd.read_json(ALL_CATEGORIES)
    return all_tasks_df, categories_df


if __name__ == '__main__':
    print('Yo daca scrii exit o sa ajungi la meniul principal, daca scrii adauga o sa incepi sa adaugi in lista taskuri')

# use test mode purely for tryiong out deletion sorting and filtering on a predefined list
    test_mode = input('test mode? yes/no: Ar trebui sa selectezi No ca sa poti incepe direct sa testezi ')
    if test_mode == 'no':
# so here we begin the script with either asking him to exit or to add, if he exits he gets to the main menu
        while True:
            option = input('Introduceti optiunea: adauga / exit: ')

            if option == 'exit':
                break
            else:
                add_task(all_tasks)

# this is the FileWritter using extinct animals
    write_files()
    all_tasks_df, categories_df = init_dataframes()

# main menu so to speak, not a menu really but within the timeframe tis all I could do
    while True:
        option = input('Introduceti optiunea: afisare / sortare / filtrare / adauga / sterge : ')
        if option == 'afisare':
            print(all_tasks_df)
# so afther the showing stops this is where the hard part begins a 2 in 1 solution to sorting and filtering
        elif option == 'sortare':
            col = input('Coloana: name/deadline/owner/category: ')
            if col not in ('name', 'deadline', 'owner', 'category'):
                print('Invalid column')
                continue

            order = input('Ordine: asc/desc: ')
            if order not in ('asc', 'desc'):
                print('Invalid order')
                continue
# minor problem here with lambda and asceding must ask for more info to Alexandra some things you just can`t find that easy
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

# yeah that was one block for filtering, showing asc/desc as the requests were made and here we can just add and delete stuff inside the list
        elif option == 'adauga':
            add_task(all_tasks)
            write_files()
            all_tasks_df, categories_df = init_dataframes()

        elif option == 'sterge':
            task_name = input('Numele task-ului de sters: ')
            all_tasks = [t for t in all_tasks if t['name'] != task_name]
            write_files()
            all_tasks_df, categories_df = init_dataframes()