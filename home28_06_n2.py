def my_zip(*iterables, strict=False):
    if strict and not all(len(x) == len(iterables[0]) for x in iterables):
        raise ValueError('Length of iterables must match in strict mode.')
    iters = [iter(i) for i in iterables]
    while True:
        try:
            current = tuple([next(it) for it in iters])
            yield current
        except StopIteration as e:
            return
    

for i in my_zip([1,2,3], [4,5,6], 'abc', strict=True):
    print(i)