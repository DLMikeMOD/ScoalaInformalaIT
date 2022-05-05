import csv
from collections import defaultdict

from numpy import average
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# import pandas as pd
#not needed anymore
import matplotlib.pyplot as plt

# og url in F String format
def get_url(day):
    return f"https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{day}-ianuarie-ora-13-00/"

#needed
browser = webdriver.Chrome(ChromeDriverManager().install())

#convert to list
date = defaultdict(list)
lista_dates = []

#the for needed for completing and parsing each link in a Fstring format by Xpath and splitting it
for day in range(20, 28):
    lista_dates.append(f'{day}')
    url = get_url(day)
    browser.get(url)
    table = browser.find_element(by=By.XPATH, value="//table[1]")
    rows = table.text.split("\n")
    header = rows[0]

#minor problems hacking and replacing
    for idx, row in enumerate(rows[1:], start=1):
        row = row.replace("Satu Mare", "Satu-Mare")
        row = row.replace("Mun. București", "București")

#counter for table rows except the last 2
        if idx <= 42:
            nr_crt, judet, cazuri, cazuri_noi, incidenta = row.split(" ")
            if cazuri_noi == '–':
                cazuri_noi = 0

            date[judet].append(
                (
                    int(cazuri.replace(".", "")),
                    int(cazuri_noi),
                    float(incidenta.replace(",", ".")),
                )
            )

# creating the final memory block and calculations for each cell
lista_cu_randuri_finale = []
for jud, valori in date.items():
    cazuri_confirmate = sum([val[0] for val in valori])
    cazuri_noi = sum([val[1] for val in valori])
    inci = round(average([val[2] for val in valori]), 2)


#sending the new headers for the table
    lista_cu_randuri_finale.append(
        {
            "Judet": jud,
            "Număr de cazuri confirmate(total) pe 7 zile": cazuri_confirmate,
            "Număr de cazuri nou confirmate pe 7 zile": cazuri_noi,
            "Incidența  înregistrată la 14 zile pe ultimele 7 zile": inci,
        }
    )


# creating the table itself using encoding on windows is a must
with open('tabel_final.csv', 'w', encoding="utf-8") as fp:
    writer = csv.DictWriter(fp, fieldnames=list(lista_cu_randuri_finale[0].keys()))
    writer.writeheader()
    writer.writerows(lista_cu_randuri_finale)