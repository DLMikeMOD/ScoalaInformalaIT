# def my_function (param_1):
#     print(type(param_1))
#     return param_1
#
# print(my_function('string', 'string1', 'string2'))
#
def numbers_sum(*var):
    suma = 0
    print(var)
    for item in var:
        suma = suma + item
    return suma

print(numbers_sum(1,2, 3, 4, 69))