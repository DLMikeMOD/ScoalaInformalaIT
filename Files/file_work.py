# with open("fisier.txt", 'w') as file:
#     file.write("Ciocanus")
#     file.close()


# with open("fisier.txt", 'r')
# try:
#     file.write("Ciocanus MAximus")
# # except Exception:
# #     pass
# finally:
#     file.close()
#
# with open("fisier1.txt", 'w') as file:   # le si creaza
#     file.write("No dilaule cum tie nu iti merge")
#
# with open("fisier2.txt", 'a') as file:
#     file.write("alt mesaj si apoi mai adaug un alt mesaj")


# with open("fisier2.txt", 'r') as file:
#     for line in file.readlines():
#         print("line", line)


with open("fisier2.txt", 'r') as file:
    for line in list(file):
        print('line', line)