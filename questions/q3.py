# The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned 
# in the sequence passed along. This function is defined in "functools" module.

from functools import reduce
nums = [1, 2, 3, 4]
x = reduce(lambda a, b: a - b, nums)
print(x)