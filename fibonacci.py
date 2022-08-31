print("Set fibonacci number:")
num = int(input())
print("output:")

def fibonacci(n):
    list = []
    go(n,list)
    for x in list[len(list)-(n+1)::]:
        print(x)

def go(n, list):
    if n <= 1:
        list.append(n)
        return n
    else:
        number = go(n - 2, list)  + go(n - 1, list)
        list.append(number)
        return number          

fibonacci(num)