# import pandas as pd
# import matplotlib.pyplot as plt
# #
# # # print(pd.__version__)
# # # a = {'x': 1, "y": 7, "z": 9}
# # # variabila = pd.Series(a, index=a.keys())
# # # variabila = pd.Series(a, index=['x', 'y'])
# # # print(variabila)
# #
# # data = {
# #     "key1": [0,1,2],
# #     "key2": [3,4,5]
# # }
# # variabila = pd.DataFrame(data, index=['linie1', 'linie2', 'linie3'])
# # # print(variabila['key2']) # valoir de pe o cheie anume din dataframe (coloana)
# # print(variabila.loc["linie2"]) #valori de pe o linie anume
#
# # df = pd.read_csv("fisier.csv")
#
# # data = {
# #   "Duration":{
# #     "0":60,
# #     "1":60,
# #     "2":60,
# #     "3":45,
# #     "4":45,
# #     "5":60
# #   },
# #   "Pulse":{
# #     "0":110,
# #     "1":117,
# #     "2":103,
# #     "3":109,
# #     "4":117,
# #     "5":102
# #   },
# #   "Maxpulse":{
# #     "0":130,
# #     "1":145,
# #     "2":135,
# #     "3":175,
# #     "4":148,
# #     "5":127
# #   },
# #   "Calories":{
# #     "0":409,
# #     "1":479,
# #     "2":340,
# #     "3":282,
# #     "4":406,
# #     "5":300
# #   }
# # }
# # df = pd.DataFrame(data)
# # print(df)
#
# df = pd.read_csv("uneven.csv")
# # print(df)
# # df1 = None
# # for x in df.index:
# #     print(df.loc[x, "AL"]) #ia coloana AL si afiseaza toate valorile de la indexul 0 pana la sf
# #     if df.loc[x, "AL"] == ':\s':
# #         df.drop(x, inplace=True)
# # print(df)
# # df1 = df.to_csv('fisier1.csv')
# # print(df.corr())
# # print(df.describe())
# # print(df.mean())
# # df.plot(kind="scatter", x="AT", y="BE")
# # df["AT"].plot(kind='hist')
# # plt.show()
# # print(df.tail(3))
# # new_df = df.dropna(inplace=True)
# df.fillna(0, inplace=True)
# print(df.fillna(0))
# # df["AL"].fillna(69, inplace=True)
# # print(df)
# # df.loc[7, "AL"]  = 666
# # print(df)
# df.replace(": ", 0, inplace=True)
# df.replace(":", 0, inplace=True)
# print(df.transpose())
# df.to_csv('fisier1.csv')


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# import pandas as pd
#
#
# def browser_function():
#     driver_path = "path/to/chromedriver"
#     chr_options = Options()
#     chr_options.add_experimental_option("detach", True)
#     chr_driver = webdriver.Chrome(driver_path, options=chr_options)
#     chr_driver.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/")
#
#
# browser = webdriver.Chrome(ChromeDriverManager().install())
# browser.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/')
# get_element = browser.find_element(by=By.XPATH, value='//*[@id="post-25121"]/div/div/table[1]/tbody')
# print(get_element.text)
# df = pd.DataFrame(get_element.text)
# df.to_csv("covid1.csv")


# current_url = "https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/"
#
# print(current_url) #prints the url of the current window.
#
# urlparamlenght = range(20, 27)
#
# current_url = current_url.replace("20", "21")
# print(current_url)

#
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


url = "https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/"


def Counterlink():
    count = 20
    while count < 28:
        count += 1
        z = url.replace("20", str(count))
        print(z)


print(Counterlink())

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(Counterlink())
table = browser.find_element(
    by=By.XPATH, value='//*[@id="post-25121"]/div/div/table[1]/tbody'
)
table_text = table.text
lista = table_text.split("\n")
header_len = browser.find_element(
    by=By.XPATH,
    value="/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr[1]/td[2]",
)
header = header_len.text.split("\n")
dictionar = {i: [] for i in header}
for j in range(0, len(header)):
    for i in range(len(header) + int(j), len(lista), len(header)):
        dictionar[header[int(j)]].append(lista[i])
print(dictionar)
df = pd.DataFrame(dictionar)
df.to_csv("Covid.csv")
