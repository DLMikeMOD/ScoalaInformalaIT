# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
#
# s=Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=s)
#
#
# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# caps = options.to_capabilities()
#
#
# browser = webdriver.Chrome(ChromeDriverManager().install())
# browser.get("https://www.bnr.ro/files/xml/nbrfxrates2021.htm")
#
#
#
# table = browser.find_element(by= By.XPATH, value ='//*[@id="Data_table"]')
# table_text = table.text
# print(table_text)
#
# def launchBrowser():
#    chrome_options = options()
#    chrome_options.binary_location="../Google Chrome"
#    chrome_options.add_argument("disable-infobars")
#    driver = webdriver.Chrome(chrome_options=chrome_options)
#
#    driver.get("https://www.bnr.ro/files/xml/nbrfxrates2021.htm")
#    while(True):
#        pass
# launchBrowser()

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.bnr.ro/files/xml/nbrfxrates2021.htm")
table = browser.find_element(by=By.XPATH, value='//*[@id="Data_table"]')
table_text = table.text
lista = table_text.split('\n')
# print(table_text)
# print(lista)
header_len = browser.find_element(by=By.XPATH, value='//*[@id="Data_table"]/table/thead/tr')
header = header_len.text.split('\n')
dictionar = {i: [] for i in header}
# print(dictionar)
for j in range (0, len(header)):
    for i in range(len(header) + int(j), len(lista), len(header)):
        # print(lista[i])
        dictionar[header[int(j)]].append(lista[i])
# print(header)
print(dictionar)
df = pd.DataFrame(dictionar)
df.to_csv("BNR all data.csv")
