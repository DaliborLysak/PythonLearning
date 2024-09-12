print("Give me all primes to number:")
number = int(input())
print("primes:")

def getPrimes(number):
    if number < 2:
        print("no primes")
        return    
    list = getBySieveOfEratosthenes(number)
    return list

def getBySieveOfEratosthenes(number):
        # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
        numbersMap = {}

        # if number is not prime set value to true
        for x in range(2,number + 1):
            numbersMap[x] = False
        
        for i in range(2,number + 1):                    
            # if is not prime continue
            if numbersMap[i] == True:
                continue

            # // start from i squared, leser numbers are collected by the way 
            actualNumber = 2
            value = i * i

            # if i squared > number finish
            if value > number:
                continue

            # process numbers
            while value < number + 1:
                numbersMap[value] = True
                actualNumber = actualNumber + 1
                value = i * actualNumber

            primes = []
            for n in range(2, len(numbersMap)):
                if numbersMap[n] == False:
                    primes.append(n)

        return primes 

print(getPrimes(number))