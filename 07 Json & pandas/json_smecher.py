# JSON- JavaScript Object Notanion
import json

import json_smecher

x = '{"name": "Ion", "age": 39, "city": "Iasi"}'
y = json.loads(x)
print(y, type(y))

z = json.dumps(y)
print(z, type(z))
a = json.dumps(["cocos", "ananas"])
b = 69
c = None
u = True
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(u, type(u))