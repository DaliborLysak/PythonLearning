# Language

help()
Ex: help(list.pop)

# types
type(x) .. return type
None .. empty type

[] .. list - mutable
[{}{}] .. dictionary - mutable
() .. tuple - imutable
{} .. set - imutable

TYPES.LIST
.append()
.pop()
.insert()


# I/O

file = open('text.txt') - open file
file.read() - read file
file.seek(0) - cursor moving
file.readlines()
file.close()

with open('text.txt', mode = 'r') as file:
  x = file.read()
  
  with open('text.txt', mode = 'w') as file:
  x = file.write('dnsfahfkjhd')
  
  mode = r,w,a,r+,w+(overwrite)
  
# conditions 

* keys *
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
  
# Loops
  
for element in list
  ...

## tuple unpacking
for a,b,c in list:
   ...
   
## dictionary unpacking
for key, value in dictionary
  ...
  
while  condition:
  ...
else:
  ...  
  
break
continue
pass - do nothing

for element in list
  pass
  
# Operators

for num in range(3,10,2) #start, end, steps
  ...
  
for element in enumerate(list) # tuples (index, item on index)
  pass
  
for element in zip(list1, list2, list3) # tuples from lists elements by shortest
  pass


# Build in Functions  
min
max

result = input("bla bla")

# list comprehensions
list = [letter for letter in stringx]
list = [num**2 for num in list if x <100]

# libraries
from random import shuffle

shuffle(list)

# functions

def name_of_function(atribute = default):
  '''
  doc string explains function
  '''
  ...
  ... 
  return ...
  
def name_of_function(*args):
  '''
  doc string explains function
  '''
  ...
  ... 
  return ...
  
def name_of_function(**kwargs):
  '''
  doc string explains function
  '''
  ...
  ... 
  return ...

# links

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

