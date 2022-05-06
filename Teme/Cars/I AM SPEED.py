import csv
import json
import pandas as pd
import os


def fisier_inp():
    some_cars = {
        "car0": {
            "id": "random",
            "brand": "Porche",
            "series": "911",
            "horses": "500",
            "price": "1900",
        },
        "car1": {
            "id": "random",
            "brand": "Porche",
            "series": "Panamera",
            "horses": "420",
            "price": "1700",
        },
        "car2": {
            "id": "random",
            "brand": "Maybach",
            "series": "F-PXD",
            "horses": "600",
            "price": "3150",
        },
        "car3": {
            "id": "random",
            "brand": "Bowler",
            "series": "Wildcat",
            "horses": "300",
            "price": "996",
        },
        "car4": {
            "id": "random",
            "brand": "Pagani Zonda",
            "series": "PSX-TURBO",
            "horses": "900",
            "price": "6900",
        },
        "car5": {
            "id": "random",
            "brand": "Bmw",
            "series": "M-4",
            "horses": "166",
            "price": "800",
        },
        "car6": {
            "id": "random",
            "brand": "Bmw",
            "series": "Z-2",
            "horses": "120",
            "price": "850",
        },
        "car7": {
            "id": "random",
            "brand": "Ferrari",
            "series": "F40",
            "horses": "400",
            "price": "2600",
        },
        "car8": {
            "id": "random",
            "brand": "Lamborghini",
            "series": "Aventador",
            "horses": "575",
            "price": "2900",
        },
        "car9": {
            "id": "random",
            "brand": "Lamborghini",
            "series": "Urus",
            "horses": "650",
            "price": "3600",
        },
        "car10": {
            "id": "random",
            "brand": "Chrysler",
            "series": "Voyager",
            "horses": "120",
            "price": "750",
        },
        "car11": {
            "id": "random",
            "brand": "Mazda",
            "series": "MX-5",
            "horses": "210",
            "price": "1989",
        },
        "car12": {
            "id": "random",
            "brand": "Jeep",
            "series": "Grand Cherokee",
            "horses": "205",
            "price": "1980",
        },
        "car13": {
            "id": "random",
            "brand": "Jeep",
            "series": "Wrangler",
            "horses": "235",
            "price": "2180",
        },
    }
    for d in some_cars.values():
        d["id"] = d["brand"][0] + d["series"][0] + d["horses"][0] + d["price"][0]
    df = pd.DataFrame(some_cars)
    df.to_csv("initial_input_list.csv")


# Trial 1
# with open('initial_input_list.csv') as fisier:
#     slow_cars = []
#     for linie in fisier:
#         tokens = linie.strip('\n').split(',')
#
#         horses = tokens[5].strip()
#
#         if horses < "120":
#             slow_cars.append(tokens)
#             print(horses)
#
#     with open('slow_cars.json', 'w') as slow_cars_fisier:
#         json.dump(slow_cars, slow_cars_fisier)


from collections import defaultdict


# Try 2
# with open('initial_input_list.csv') as fisier:
#     reader = csv.DictReader(fisier)
#     category_dict = defaultdict(list)
#     print(category_dict)

# for line in reader:
#     for key, value in line.items():
#         line[key] = value.strip()
#
#     category = some_cars.values()
#     category_dict[category].append(line)

# print(json.dumps(category_dict, indent=4))
#
# with open('category_cars.json', 'w') as old_cars_fisier:
#     json.dump(category_dict, old_cars_fisier)
#
# with open('category_cars.json') as old_cars_fisier:
#     category_dict_din_fisier = json.load(old_cars_fisier)
#
# print(json.dumps(category_dict_din_fisier, indent=4))
#
# for category, items_list in category_dict.items():
#     print(category, items_list)
#     with open(f'{category}_cars.json', 'w') as category_fisier:
#         json.dump(items_list, category_fisier)

# final try
def make_folder():
    directory = "results"
    parent_dir = r"C:\Users\DLMike\PycharmProjects\ScoalaInformalaIT\Teme\Cars"
    path = os.path.join(parent_dir, directory)
    try:
        os.mkdir(path)
    except OSError:
        pass


#
#
def main_func():
    fisier_inp()
    df = pd.read_csv("initial_input_list.csv")

    # revert
    df = df.T
    # DataFrame values
    df = pd.DataFrame(df.values, columns=["id", "brand", "series", "horses", "price"])
    # removal and check
    df = df.drop(df.index[0])
    df.horses = pd.to_numeric(df.horses)
    df.price = pd.to_numeric(df.price)

    # Speed model
    slow_cars = df[df.horses < 200]
    slow_cars.to_json(r"results\slow_cars.json")

    fast_cars = df[(df.horses >= 200) & (df.horses < 300)]
    fast_cars.to_json(r"results\fast_cars.json")

    super_cars = df[df.horses >= 180]
    super_cars.to_json(r"results\super_cars.json")

    # Pricing model
    cheap_cars = df[df.price < 1000]
    cheap_cars.to_json(r"results\cheap_cars.json")

    medium_cars = df[(df.price >= 1000) & (df.horses < 5000)]
    medium_cars.to_json(r"results\mid-range_cars.json")

    expensive_cars = df[df.price >= 5000]
    expensive_cars.to_json(r"results\high-end_cars.json")

    # Branding files
    porche = df.sort_values(by="brand")
    filters = porche["brand"].str.contains("Porche")
    porche = porche.loc[filters]
    porche.to_json(r"results\Porche.json")

    maybach = df.sort_values(by="brand")
    filters = maybach["brand"].str.contains("Maybach")
    maybach = maybach.loc[filters]
    maybach.to_json(r"results\Maybach.json")

    bowler = df.sort_values(by="brand")
    filters = bowler["brand"].str.contains("Bowler")
    bowler = bowler.loc[filters]
    bowler.to_json(r"results\Bowler.json")

    zonda = df.sort_values(by="brand")
    filters = zonda["brand"].str.contains("Zonda")
    zonda = zonda.loc[filters]
    zonda.to_json(r"results\Pagani Zonda.json")

    bwm = df.sort_values(by="brand")
    filters = bwm["brand"].str.contains("BMW")
    bwm = bwm.loc[filters]
    bwm.to_json(r"results\BMW.json")

    ferr = df.sort_values(by="brand")
    filters = ferr["brand"].str.contains("Ferrari")
    ferr = ferr.loc[filters]
    ferr.to_json(r"results\Ferrari.json")

    lambo = df.sort_values(by="brand")
    filters = lambo["brand"].str.contains("Lamborghini")
    lambo = lambo.loc[filters]
    lambo.to_json(r"results\Lamborghini.json")

    chry = df.sort_values(by="brand")
    filters = chry["brand"].str.contains("Chrysler")
    chry = chry.loc[filters]
    chry.to_json(r"results\Chrysler.json")

    mazda = df.sort_values(by="brand")
    filters = mazda["brand"].str.contains("Mazda")
    mazda = mazda.loc[filters]
    mazda.to_json(r"results\Mazda.json")

    jeep = df.sort_values(by="brand")
    filters = jeep["brand"].str.contains("Jeep")
    jeep = jeep.loc[filters]
    jeep.to_json(r"results\Jeep.json")

    # Filtering user inpot must add additiona values but mek is short

    # df = df.sort_values(by='price')
    # print(df['price'])

    df = df.sort_values(by="brand")
    print(df["brand"])

    # df = df.sort_values(by='horses')
    # print(df['horses'])

    search = input("Cauta dupa un brand in baza de date\n> ").capitalize()
    # find it
    filters = df["brand"].str.contains(search)
    df = df.loc[filters]
    # and show it
    print(f"Avem aceste modele in baza de date: {df}")

    # trying a redirect to a loop
    # while search is not False:
    #     retry = input("Doresti sa cauti din nou? (da,nu)")
    #     if retry == 'da':
    #         search = input('Cauta dupa un brand in baza de date\n> ').capitalize()
    #         filters = df['brand'].str.contains(search)
    #         df = df.loc[filters]
    #         print(f"Avem acest model in baza de date: {df}")
    #     else:
    #         break

    # make a file to use in "sales"
    df.to_json(r"results\cautare_client.json")


# the soul
if __name__ == "__main__":
    main_func()
