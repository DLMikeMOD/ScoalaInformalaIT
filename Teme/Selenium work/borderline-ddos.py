# import csv
# from collections import defaultdict
#
# from numpy import average
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# # import pandas as pd
# import matplotlib.pyplot as plt
#
# # og url in F String format
# def get_url(day):
#     return f"https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{day}-ianuarie-ora-13-00/"
#
# #needed
# browser = webdriver.Chrome(ChromeDriverManager().install())
#
# #convert to list
# date = defaultdict(list)
# lista_dates = []
#
# #the for needed for completing and parsing each link in a Fstring format by Xpath and splitting it
# for day in range(20, 28):
#     lista_dates.append(f'{day}')
#     url = get_url(day)
#     browser.get(url)
#     table = browser.find_element(by=By.XPATH, value="//table[1]")
#     rows = table.text.split("\n")
#     header = rows[0]
#
# #minor problems hacking and replacing
#     for idx, row in enumerate(rows[1:], start=1):
#         row = row.replace("Satu Mare", "Satu-Mare")
#         row = row.replace("Mun. București", "București")
#
# #counter for table rows except the last 2
#         if idx <= 42:
#             nr_crt, judet, cazuri, cazuri_noi, incidenta = row.split(" ")
#             if cazuri_noi == '–':
#                 cazuri_noi = 0
#
#             date[judet].append(
#                 (
#                     int(cazuri.replace(".", "")),
#                     int(cazuri_noi),
#                     float(incidenta.replace(",", ".")),
#                 )
#             )
#
# # creating the final memory block and calculations for each cell
# lista_cu_randuri_finale = []
# for jud, valori in date.items():
#     cazuri_confirmate = sum([val[0] for val in valori])
#     cazuri_noi = sum([val[1] for val in valori])
#     inci = round(average([val[2] for val in valori]), 2)
#
#
# #sending the new headers for the table
#     lista_cu_randuri_finale.append(
#         {
#             "Judet": jud,
#             "Număr de cazuri confirmate(total) pe 7 zile": cazuri_confirmate,
#             "Număr de cazuri nou confirmate pe 7 zile": cazuri_noi,
#             "Incidența  înregistrată la 14 zile pe ultimele 7 zile": inci,
#         }
#     )
#
#
# # creating the table itself using encoding on windows is a must
# with open('tabel_final.csv', 'w', encoding="utf-8") as fp:
#     writer = csv.DictWriter(fp, fieldnames=list(lista_cu_randuri_finale[0].keys()))
#     writer.writeheader()
#     writer.writerows(lista_cu_randuri_finale)
#

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pandas as pd


base_url = 'https://www.mai.gov.ro/'
date_targetate = [20, 21, 22, 23, 24, 25, 26];
luna_targetata = 'ianuarie'


def exclude_first_element(list):
    del list[0]


def exclude_last_element(list):
    del list[-1]


def create_url_param(data, luna):
    return f'informare-covid-19-grupul-de-comunicare-strategica-{data}-{luna}-ora-13-00'


def create_url(data, luna):
    return f'{base_url}{create_url_param(data,luna)}'

browser = webdriver.Chrome(ChromeDriverManager().install())


def get_requests(data):
    url = create_url(data, luna_targetata)
    browser.get(url)
    table_rows = browser.find_elements(by=By.XPATH, value='//table[contains(.,"Număr de cazuri nou confirmate")]/tbody//tr')
    exclude_first_element(table_rows)
    exclude_last_element(table_rows)

    cazuri = []

    for row in table_rows:
        elements = row.find_elements(by=By.TAG_NAME, value='td')
        nume_judet = elements[1].text
        cazuri_noi = elements[3].text or '-'
        cazuri.append({nume_judet: cazuri_noi})

    return cazuri


def preia_cazuri():
    rezultat = []
    for data in date_targetate:
        istoric_cazuri = get_requests(data)
        rezultat.append({data: istoric_cazuri})
    return rezultat


def main():
     cazuri = preia_cazuri()
     df = pd.DataFrame(cazuri)
     df.to_csv("Covid.csv")


main()