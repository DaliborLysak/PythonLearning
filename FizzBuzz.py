for x in range(1, 101):
    str = ''
    
    if x % 3 == 0:
        str += "Fizz"
        
    if x % 5 == 0:
        str +="Buzz"
        
    if not x % 3 == 0 and not x % 5 == 0:
        str = x
        
    print(str)