#map function

def my_map(func, iterable):
    for i in iterable:
        yield func(i)
new = list(my_map(lambda x : x ** 2 , [1 , 2 ,  3 , 4]))
print(new)

