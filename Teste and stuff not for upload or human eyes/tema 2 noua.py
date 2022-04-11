# import csv
# import datetime
# ​
# # crearea fisierului care contine categoriile de task-uri
# ​
# categorii = [
#     ['curs'],
#     ['cumparaturi'],
#     ['munca'],
#     ['cadouri']
# ]
# ​
# with open('categorii.csv', 'w') as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=',')
#     for categorie in categorii:
#         csv_writer.writerow(categorie)
# csv_file.close()
# ​
# ​
# def validate_date(data_introdusa):
#     try:
#         datetime.datetime.strptime(data_introdusa, "%d.%m.%Y")
#     except ValueError as e:
#         print("ERROR DATE\n", e)
#         return False
#     return True
# ​
# ​
# def validate_hour(ora_introdusa):
#     try:
#         datetime.datetime.strptime(ora_introdusa, "%H:%M")
#     except ValueError as e:
#         print("ERROR TIME\n", e)
#         return False
#     return True
# ​
# ​
# def validate_task(task):
#     with open ("taskuri_deadline_responsabil_categorie.txt", 'r') as file:
#         for line in file.readlines():
#             if task in line:
#                 print("Task already in file")
#                 return False
#         return True
# ​
# ​
# def validate_responsabil(responsabil):
#    if responsabil.isalpha() == True:
#        return True
#    print("Name must be a string")
#    return False
# ​
# # cerinte
# ​
# ​
# def cerinte():
#     raspuns_utilizator = input("Doresti sa introduci un task? (yes/no) ")
#     while raspuns_utilizator != 'no':
#         with open('taskuri_deadline_responsabil_categorie.txt', 'a') as file:
#             task = input("Introduceti un task: ")
#             if validate_task(task) == False:
#                 break
# ​
#             deadline = input("Introduceti o data limita pentru rezolvarea task-ului: ")
#             if validate_date(deadline) == False:
#                 break
#             hour_deadline = input("Introduceti o ora limita pentru rezolvarea task-ului: ")
#             if validate_hour(hour_deadline) == False:
#                 break
# ​
#             responsabil = input("Introduceti numele persoanei responsabile pentru task-ul introdus anterior: ")
#             if validate_responsabil(responsabil) == False:
#                 break
# ​
#             cateogrie_task = input("Introduceti categoria din care face parte task-ul introdus: ")
#             c = [cateogrie_task]
#             if c not in categorii:
#                 print("Cateogria introdusa nu exista!")
# ​
#             file.write(task)
#             file.write(",")
#             file.write(deadline)
#             file.write(" ")
#             file.write(hour_deadline)
#             file.write(",")
#             file.write(responsabil)
#             file.write(",")
#             file.write(cateogrie_task)
#             file.write("\n")
# ​
#             raspuns_utilizator = input("Doresti sa introduci un task? (yes/no) ")
# ​
# ​
# # cerinte()
# ​
# # cerinte suplimentare
# ​
# # 1. Listare date: în afișarea inițială a datelor se realizează o sortare în funcție de categorie.
# def listare_date():
#     print("Listarea datelor\n")
#     with open("taskuri_deadline_responsabil_categorie.txt", 'r') as file:
#         informatii = file.readlines()
# ​
#         for line in sorted(informatii, key = lambda line: line.split(",")[3]):
#             print (line)
# ​
# # listare_date()
# ​
# # 2. Sortare: se alege o opțiune din cele 8 de mai jos:
# def sortare_asc_task():
#     print("Sortare ascendenta task\n")
#     with open("taskuri_deadline_responsabil_categorie.txt", 'r') as file:
#          informatii = file.readlines()
# ​
#          for line in sorted(informatii, key=lambda line: line.split(",")[0]):
#             print(line)
# ​
# # sortare_asc_task()
# ​
# ​
# def sortare_desc_task():
#     print("Sortare descendenta task\n")
#     with open("taskuri_deadline_responsabil_categorie.txt", 'r') as file:
#         informatii = file.readlines()
# ​
#         for line in sorted(informatii, key=lambda line: line.split(",")[0], reverse = True ):
#              print(line)
# ​
# # sortare_desc_task()
# ​
# def sortare_asc_data():
#     print("Sortare ascendenta data\n")
#     with open("taskuri_deadline_responsabil_categorie.txt", 'r') as file:
#         informatii = file.readlines()
#         for line in informatii:
#             date = line.split()[1].split(".")
#             hour = line.split()[2].split(":")
#             date = datetime.datetime(int(date[2]), int(date[1]), int(date[0]), int(hour[0]), int(hour[1][:-1]))
#             indexing = informatii.index(line)
#             informatii[indexing] = line.split(",")
#             informatii[indexing][1] = date
# ​
#         for line in sorted(informatii, key=lambda line: line[1]):
#             line[1] = line[1].__str__()   # conversie din datetime in str
# ​
#             print(", ".join(line))
# ​
# # sortare_asc_data()
# ​
# def sortare_desc_data():
#     print("Sortare descendenta data\n")
#     with open("taskuri_deadline_responsabil_categorie.txt", 'r') as file:
#         informatii = file.readlines()
#         for line in informatii:
#             date = line.split()[1].split(".")
#             hour = line.split()[2].split(":")
#             date = datetime.datetime(int(date[2]), int(date[1]), int(date[0]), int(hour[0]), int(hour[1][:-1]))
#             indexing = informatii.index(line)
#             informatii[indexing] = line.split(",")
#             informatii[indexing][1] = date
# ​
#         for line in sorted(informatii, key=lambda line: line[1], reverse = True):
#             line[1] = line[1].__str__()   # conversie din datetime in str
# ​
#             print(", ".join(line))
# ​
# def sortare_asc_responsabil():
#     print("Sortare ascendenta responsabil\n")
#     with open("taskuri_deadline_responsabil_categorie.txt", 'r') as file:
#         informatii = file.readlines()
# ​
#         for line in sorted(informatii, key=lambda line: line.split(",")[2]):
#             print(line)
# ​
# # sortare_asc_responsabil()
# ​
# def sortare_desc_responsabil():
#     print("Sortare descendenta responsabil\n")
#     with open("taskuri_deadline_responsabil_categorie.txt", 'r') as file:
#         informatii = file.readlines()
# ​
#         for line in sorted(informatii, key=lambda line: line.split(",")[2], reverse = True):
#             print(line)
# ​
# # sortare_desc_responsabil()
# ​
# def sortare_asc_cateogrie():
#     print("Sortare ascendenta categorie\n")
#     with open("taskuri_deadline_responsabil_categorie.txt", 'r') as file:
#         informatii = file.readlines()
# ​
#         for line in sorted(informatii, key=lambda line: line.split(",")[3]):
#             print(line)
# ​
# # sortare_asc_cateogrie()
# ​
# def sortare_desc_cateogrie():
#     print("Sortare descendenta categorie\n")
#     with open("taskuri_deadline_responsabil_categorie.txt", 'r') as file:
#         informatii = file.readlines()
# ​
#         for line in sorted(informatii, key=lambda line: line.split(",")[3], reverse = True):
#             print(line)
# ​
# # sortare_desc_cateogrie()
# ​
# # 3.Filtrare date:
# # filtrarea datelor reprezintă de fapt o listare a datelor în funcție de anumite detalii date de la tastatură.
# # criteriile de filtrare sunt: task, data, responsabil, categorie
# # se cere de la tastatura campul dupa care se va face filtarea
# ​
# # def filter_task():
# ​
# # def filter_data():
# ​
# # def filter_responsabil():
# ​
# # def filter_categorie():
# ​
# # alegere tip filtrare
# ​
# # def choose_filter_type();
# ​
# # def add_new_task():
# ​
# # def edit_task():
# ​
# # def remove_task():
# ​
# def meniu_operatii():
#     print("Meniu de operatii")
#     print("1.Listare date\n")
#     print("2.sortare ascendentă task\n")
#     print("3. sortare descendentă task\n")
#     print("4.sortare ascendentă data\n")
#     print("5. sortare descendentă data\n")
#     print("6.sortare ascendentă persoana responsabila\n")
#     print("7. sortare descendentă persoana responsabila\n")
#     print("8.sortare ascendentă categorie\n")
#     print("9. sortare descendentă categorie\n")
#     print("10.Filtrare date\n")
#     print("11.Adaugare nou task\n")
#     print("12.Editare task\n")
#     print("13.Stergere task\n")
#     print("0. Exit\n")
# ​
#     comenzi = \
#     {
#         "0":exit,
#         "1":listare_date,
#         "2":sortare_asc_task,
#         "3":sortare_desc_task,
#         "4":sortare_asc_data,
#         "5":sortare_desc_data,
#         "6":sortare_asc_responsabil,
#         "7":sortare_desc_responsabil,
#         "8":sortare_asc_cateogrie,
#         "9":sortare_desc_cateogrie,
#         "10":"10.Filtrare date\n",
#         "11":"11.Adaugare nou task\n",
#         "12":"12.Editare task\n",
#         "13":"13.Stergere task\n",
#     }
# ​
#     operatie ="14"
# ​
#     while operatie != "0":
#         operatie =input("Introduceti numarul operatiei pe care doriti sa o realizati:")
#         comenzi[operatie]()
# ​
# meniu_operatii()
# ​
# # case mare cu toate optiunile meniului


import datetime
import json
import pandas as pd

option = None

EXIT_KEYWORD = 'exit'

print("Introdu ce trebuie si apoi exit ca sa inchzi programul")

categories = ['fizic', 'work', 'cooking', 'shopping']
all_tasks = []


while True:
    option = input("Introduceti optiunea: adauga/Exit")

    if option == "exit":
        break
    else:
        task_name = input("Nume Task: ")

    if task_name in [t['name']] for t in all_tasks]:
        print("Taskl deja exista")
        continue

    task_date = input("Introdu Data: ")
    task_owner = input("Responsabil Task: ")
    category = input("Categorie Task: ")

    if category not in categories:
        print("Categoria nu exista, categoriile valide sunt : {categories}")
        continue

    all_tasks.append(
        dict (
            name=task_name, deadline=task_date, owner=task_owner, category=category
        )
    )

ALL_TASKS_PATH = 'all_tasks.json'
ALL_CATEGORIES = 'all_categories.json'

with open(ALL_TASKS_PATH, 'w')as fw:
    json.dump(all_tasks, fw)

with open(ALL_CATEGORIES, 'w') as fw:
    json.dump(categories, fw)

all_tasks_df = pd.read_json(ALL_TASKS_PATH)
categories_df = pd.read_json(ALL_CATEGORIES)