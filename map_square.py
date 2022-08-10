list2 = [4,5,2,9]

def func(i):
    return i**2

y = list(map(func,list2))
print(y)

# z = list(map((lambda a : a**2), list2))
# print(z)