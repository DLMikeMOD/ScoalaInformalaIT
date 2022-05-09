import csv
import json

# University way
# with open('10feb/input.csv') as fisier:
#     old_cars = []
#     for linie in fisier:
#         tokens = linie.strip('\n').split(',')
#
#         categorie = tokens[5].strip()
#
#         if categorie == 'old':
#             old_cars.append(tokens)
#             print(categorie)
#
#     with open('10feb/old_cars.json', 'w') as old_cars_fisier:
#         json.dump(old_cars, old_cars_fisier)

# Advanced way
from collections import defaultdict

with open('input.csv') as fisier:
    reader = csv.DictReader(fisier)
    category_dict = defaultdict(list)

    for line in reader:
        for key, value in line.items():
            line[key] = value.strip()

        category = line['categorie']
        category_dict[category].append(line)


# print(json.dumps(category_dict, indent=4))

with open('category_cars.json', 'w') as old_cars_fisier:
    json.dump(category_dict, old_cars_fisier)


with open('category_cars.json') as old_cars_fisier:
    category_dict_din_fisier = json.load(old_cars_fisier)

# print(json.dumps(category_dict_din_fisier, indent=4))

for category, items_list in category_dict.items():
    print(category, items_list)
    with open(f'{category}_cars.json', 'w') as category_fisier:
        json.dump(items_list, category_fisier)
