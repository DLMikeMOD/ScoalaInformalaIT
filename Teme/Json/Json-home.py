import random
from collections import defaultdict
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

description = (
    'Country',
    ['2011 ', '2012 ', '2013 ', '2014 ', '2015 ', '2016 ', '2017', '2018 ', '2019 '],
)
dataset = [
    ('AL', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '84 ', ': ']),
    ('AT', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ', '89 ', '90 ']),
    ('BA', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '69 ', '72 ']),
    ('BE', ['77 ', '78 ', '80 ', '83 ', '82 ', '85 ', '86 ', '87 ', '90 ']),
    ('BG', ['45 ', '51 ', '54 ', '57 ', '59 ', '64 ', '67 ', '72 ', '75 ']),
    ('CH', [': ', ': ', ': ', '91 ', ': ', ': ', '93 b', ': ', '96 ']),
    ('CY', ['57 ', '62 ', '65 ', '69 ', '71 ', '74 ', '79 ', '86 ', '90 ']),
    ('CZ', ['67 ', '73 ', '73 ', '78 ', '79 ', '82 ', '83 ', '86 ', '87 ']),
    ('DE', ['83 ', '85 ', '88 ', '89 ', '90 ', '92 ', '93 ', '94 ', '95 ']),
    ('DK', ['90 ', '92 ', '93 ', '93 ', '92 ', '94 ', '97 ', '93 ', '95 ']),
    ('EA', ['74 ', '76 ', '79 ', '81 ', '83 ', '85 ', '87 ', '89 ', '90 ']),
    ('EE', ['69 ', '74 ', '79 ', '83 ', '88 ', '86 ', '88 ', '90 ', '90 ']),
    ('EL', ['50 ', '54 ', '56 ', '66 ', '68 ', '69 ', '71 ', '76 ', '79 ']),
    ('ES', ['63 ', '67 ', '70 ', '74 ', '79 ', '82 ', '83 ', '86 ', '91 ']),
    ('FI', ['84 ', '87 ', '89 ', '90 ', '90 ', '92 ', '94 ', '94 ', '94 ']),
    ('FR', ['76 ', '80 ', '82 ', '83 ', '83 ', '86 ', '86 ', '89 ', '90 ']),
    ('HR', ['61 ', '66 ', '65 ', '68 ', '77 ', '77 ', '76 ', '82 ', '81 ']),
    ('HU', ['63 ', '67 ', '70 ', '73 ', '76 ', '79 ', '82 ', '83 ', '86 ']),
    ('IE', ['78 ', '81 ', '82 ', '82 ', '85 ', '87 ', '88 ', '89 ', '91 ']),
    ('IS', ['93 ', '95 ', '96 ', '96 ', ': ', ': ', '98 ', '99 ', '98 ']),
    ('IT', ['62 ', '63 ', '69 ', '73 ', '75 ', '79 ', '81 ', '84 ', '85 ']),
    ('LT', ['60 ', '60 ', '65 ', '66 ', '68 ', '72 ', '75 ', '78 ', '82 ']),
    ('LU', ['91 ', '93 ', '94 ', '96 ', '97 ', '97 ', '97 ', '93 ', '95 ']),
    ('LV', ['64 ', '69 ', '72 ', '73 ', '76 ', '77 b', '79 ', '82 ',  '85 ']),
    ('ME', [': ', '55 ', ': ', ': ', ': ', ': ', '71 ', '72 ', '74 ']),
    ('MK', [': ', '58 ', '65 ', '68 ', '69 ', '75 ', '74 ', '79', '82']),
    ('MT', ['75 ', '77 ', '78 ', '80 ', '81 ', '81 ', '85 ', '84 ', '86 ']),
    ('NL', ['94 ', '94 ', '95 ', '96 ', '96 ', '97 ', '98 ', '98 ', '98 ']),
    ('NO', ['92 ', '93 ', '94 ', '93 ', '97 ', '97 ', '97 ', '96 ', '98 ']),
    ('PL', ['67 ', '70 ', '72 ', '75 ', '76 ', '80 ', '82 ', '84 ', '87 ']),
    ('PT', ['58 ', '61 ', '62 ', '65 ', '70 ', '74 ', '77 ', '79 ', '81 ']),
    ('RO', ['47 ', '54 ', '58 ', '61 b', '68 ', '72 ', '76 ', '81 ', '84 ']),
    ('RS', [': ', ': ', ': ', ': ', '64 ', ': ', '68 ', '73 ', '80 ']),
    ('SE', ['91 ', '92 ', '93 ', '90 ', '91 ', '94 b', '95 ', '93 ', '96 ']),
    ('SI', ['73 ', '74 ', '76 ', '77 ', '78 ', '78 ', '82 ', '87 ', '89 ']),
    ('SK', ['71 ', '75 ', '78 ', '78 ', '79 ', '81 ', '81 ', '81 ', '82 ']),
    ('TR', [': ', '47 ', '49 ', '60 ', '70 ', '76 ', '81 ', '84 ', '88 ']),
    ('UK', ['83 ', '87 ', '88 ', '90 ', '91 ', '93 ', '94 ', '95 ', '96 ']),
    ('XK', [': ', ': ', ': ', ': ', ': ', ': ', '89 ', '93 ', '93 ']),
]

#Testing here different methods
# all = []
# for c, d in dataset:
#     X = [int(dd[-1]) for dd in d]
#     all.append(X)
#
# y = [c for c, _ in dataset]

# x = []
# y = []
# area = []
# colors = []
#
# for i in range(1000):
#     g = random.randrange(1, 10)
#     x.append(g)
#     y.append(g)
#     area.append(g)
#     colors.append(g)
#
#
# freq_dict = defaultdict(int)
#
# for nr in x:
#     freq_dict[nr] += 1
#
#
# plt.scatter(x, y, s=area, c=colors, alpha=0.5)
# plt.show()
#end


ddict = {}
ddict[description[0]] = ddict.get(description[0], description[1])
first = []
second = []
for j in dataset:
    first.append(j[0][0:])
    second.append(j[1])
    ddd = dict(zip(first, second))
    caller = {}

# seems to work but pycharms says it as an error
for i in [ddict, ddd]:
    caller.update(i)
    df = pd.DataFrame(caller)
    df = df.T
    #inspired regex fix here
    df.replace(r'[a-zA-Z]|[\s]', '', regex=True, inplace=True)
    df.replace(':', 0, inplace=True)
    df.apply(pd.to_numeric)
    df = df.astype(float)
    df.loc['mean'] = df.mean(axis=0)
    df = df.T
    print(df)

#scatman
plt.scatter(df.AL.mean(), df.AT.mean())
plt.show()
df.plot.scatter(x='AL', y='AT')
plt.show()
df['RO'].plot.hist()
plt.show()

# data to csv and explain
df.to_csv('sumtabel.csv')
print(df.describe())


def country_avg(x):
    y = df[x].mean()
    return y
print(country_avg('RO'))


x = [int(d[-1].strip()) if d[-1] != ': ' else 0 for _, d in dataset]
print(x)
num_bins = len(x)
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
plt.show()

#Clean
plt.clf()

# def year_data(x, y):
#     df = pd.DataFrame(x)
#     df = df.T
#     df = df[y]
#     return df
# print(year_data(caller, 8))

# def country_date(x, y):
#     df = pd.DataFrame(x)
#     df = df['Country'] + df[y]
#     return df
# print(country_date(caller, 'RO'))
