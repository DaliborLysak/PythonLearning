# def f(a, b=5, c=None):
#     if c is None:
#         c = []
#     c.append(a + b)
#     return c

# print(f(1), f(2))

# try:
#     x=int("hello")
# except ValueError:
#     print("Caught a ValueError")

# class TestClass:
#     def __init__(self, value):
#         self.value = value

# object = TestClass(10)
# object.value = 20
# print(object.value)

for i in range(3):
    print(i)
else:
    print("Loop completed without break")
