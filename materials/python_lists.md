# Python Lists

# unpacking with \*

```python
a, *b, c = [1,2,3,4,5]
print(a, b, c)
```

```cmd
1 [2, 3, 4] 5
```

# chained assigment

```python
a=b=[]
a.append(1)
print(b)
```

```cmd
[1]
```

# is vs ==

```python
a = [1,2,3]
b = [1,2,3]
print(a == b)
print(a is b)
```

```cmd
True
False
```

# zip()

```python
a = ["a","b","c"]
b = [1,2,3]
for a,b in zip(a,b):
    print(f"{a}:{b}")
```

```cmd
a:1
b:2
c:3
```

# list comprehensions

```python
squares = [x**2 for x in range(10)]
print(squares)
```

```cmd
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

# enumerate using

```python
a = ["a","b","c"]
for index, value in enumerate(a):
    print(index, value)
```

```cmd
0 a
1 b
2 c
```
