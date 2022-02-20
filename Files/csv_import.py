import csv

masini = [
    ['Dacia', 'Logan', 2005, 75],
    ['Renault', 'Meganne', 2010, 100]
]


with open('data.csv', 'a') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    for masina in masini:
        csv_writer.writerow(masina)