# Language

help()

```python
help(list.pop)
```

## types

type(x) .. return type
None .. empty type

[{}{}] .. dictionary - mutable
() .. tuple - imutable

### string slicing

```python
# String slicing
String = 'ASTRING'

# Using slice constructor
s1 = slice(3)
s2 = slice(1, 5, 2)
s3 = slice(-1, -12, -2)

print("String slicing")
print(String[s1])
print(String[s2])
print(String[s3])

# String slicing
# AST
# SR
# GITA
```

### set

{} .. set - imutable

_empty set_ - x=set()

_add elements from list_ - x.update(list)

### list

[] .. list - mutable
.append()
.pop()
.insert()

## I/O

file = open('text.txt') - open file
file.read() - read file
file.seek(0) - cursor moving
file.readlines()
file.close()

```python
with open('text.txt', mode = 'r') as file:
  x = file.read()
```

```python
with open('text.txt', mode = 'w') as file:
  x = file.write('dnsfahfkjhd')
```

mode = r,w,a,r+,w+(overwrite)

## conditions

and
or
not

if
elseif
else

in

if condition:
...
elseif condition:
...
end:
...

## Loops

for element in list
...

### tuple unpacking

```python
for a,b,c in list:
...
```

```python
x =(1,2)
a,b = x
```

### dictionary unpacking

for key, value in dictionary
...

while condition:
...
else:
...

break
continue
pass - do nothing

for element in list
pass

## Operators

for num in range(3,10,2) #start, end, steps
...

for element in enumerate(list) # tuples (index, item on index)
pass

for element in zip(list1, list2, list3) # tuples from lists elements by shortest
pass

## Build in Functions

min
max

result = input("bla bla")

## list comprehensions

```python
list = [letter for letter in stringx]
```

```python
list = [num**2 for num in list if x <100]
```

## libraries

**system variables**

- C:\Users\lysak\AppData\Local\Programs\Python\Python312
- C:\Users\lysak\AppData\Local\Programs\Python\Python312\Scripts

**instalation**

```bash
pip install requests
```

**using**

```python
from random import shuffle

shuffle(list)
```

## functions

def name_of_function(atribute = default):
'''
doc string explains function
'''
...
...
return ...

def name_of_function(\*args):
'''
doc string explains function
'''
...
...
return ...

def name_of_function(\*\*kwargs):
'''
doc string explains function
'''
...
...
return ...

## map

map(function, collection)

```python
for i in map(function, collection)
```

```python
list(map(function, collection))
```

## filter

```python
list(filter(function, collection))
```

## lambda

```python
lambda x: return x**2
```

## global varialbe

```python
def func():
  global x
```

## main script identification

```python
if name == "_main_":
```

## oop 

### classes

```python
class NameOfClass(AncestorClass):

  # static
  global_param = 'static'

  # constructor
  def __init__(self, param='default'):
    AncestorClass.__init__(self)
    self.param = param

c = NameOfClass(param = 'param')
```

### delete instance

```python
del c
```
## exceptions

```python
try:
except:
except:
else:
finally:
```

## links

Basic Practice:

http://codingbat.com/python

More Mathematical (and Harder) Practice:

https://projecteuler.net/archives

List of Practice Problems:

http://www.codeabbey.com/index/task_list

A SubReddit Devoted to Daily Practice Problems:

https://www.reddit.com/r/dailyprogrammer

A very tricky website with very few hints and touch problems (Not for beginners but still interesting)

http://www.pythonchallenge.com/
