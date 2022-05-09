# my_lambda = lambda x, y: x + y
# # denumire_functie = lambda param1, param2: corp_functie
# my_sum = my_lambda(6, 9)
# print(my_sum)
#
# def my_lambda(x, y):
#     return x + y

# diferenta = lambda x, y, z: x - y - z
# dif = diferenta(4,3, 199)
# print(dif)

players = [{
    "first_name": "Marian",
    "last_name": "Valorosul",
    "varsta": 12
},
    {
    "first_name": "Ionci",
    "last_name": "Pulio",
    "varsta": 15
    },
    {
    "first_name": "Pisti",
    "last_name": "Smecherul",
    "varsta": 18
    }
]

jucatori_sortati = sorted(players, key=lambda jucator: player["varsta"])
print(jucatori_sortati)