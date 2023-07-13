#counter
def counter():
    count = 0
    def inner_f():
        nonlocal count;
        count += 1
        return count
    return inner_f
res = counter()
print(res())
print(res())
print(res())
print(res())

        