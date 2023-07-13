#enumerate inplementation
def my_enumerate(iterable , start = 0):
    count = start
    for i in iterable:
        yield (count , i)
        count += 1
m =my_enumerate([2 ,6 , 7, 9])
for i in m:
    print(i)