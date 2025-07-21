def func():
    for i in range(10):
        if i > 3:
            return
        yield i

print(list(func()))