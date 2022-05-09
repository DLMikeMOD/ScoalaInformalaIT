import pandas as pd

# dictionar_date = {
#     "masini": ['Dacia', 'BMW', 'Porche', 'Bowler'],
#     "culoare": ['alb', 'albastru', 'rosu', 'gri'],
#
# }
#
# variabila = pd.DataFrame(dictionar_date)
# print(variabila)

#
# masini = ['Dacia', 'BMW', 'Porche', 'Bowler']
# variabila = pd.Series(masini, index=["x", "y", "z", "q"])
# print(variabila)# add [0]- manual index to show only set value
# print(variabila[0])
#
# masini = {"x": "Dacia", "y": "Porche","z": "BMW", }
# variabila = pd.Series(masini, index=["y", "z"])
# print(variabila)


# dictionar_date = {
#     "masini": ['Dacia', 'BMW', 'Porche', 'Bowler'],
#     "culoare": ['alb', 'albastru', 'rosu', 'gri'],
#
# }
#
# variabila = pd.DataFrame(dictionar_date, index=["producator1", "producator2", "producator3", "producator4"])
# # print(variabila.loc[[0, 1]])
# # print(variabila.loc["producator1"])
# print(variabila.loc[["producator1", "producator2"]])
#
# with open('07/Json & pandas/newjson.json', 'w') as newjason:
#     json.dump(category_dict, newjason)

data ={
  "producatori1": {
    "masini": "Dacia",
    "culoare": "alb"
  ,
    "producatori2": {
    "masini": "Porche",
    "culoare": "rosu"
  },
    "producatori3": {
    "masini": "BMW",
    "culoare": "albastru"
  }
}
}
url = 'https://api.exchangerate-api.com/v4/latest/USD'
variabila1 = pd.read_json(url)
# variabila1 = pd.read_json("data.json")
print(variabila1)
variabila1 = pd.DataFrame(data)
fisier = variabila1.to_csv("noul.csv")