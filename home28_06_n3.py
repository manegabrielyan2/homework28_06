#filter implementation

def my_filterr(function , iterable):
    if function == None:
        for i in iterable:
            if i:
                yield i
    else:
        for i in iterable:
            if function(i):
                yield(i)
lst = list(my_filterr(lambda x : x % 2 == 0 , [0 , 9 , 8 , 0 , 56]))
print(lst)