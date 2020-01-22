# problemName = "Largest prime factor"
# problemNum = 3
# solutionBy = "FIGBERT"
# language = "Python"
# dateCompleted = "21/01/2020"
import math

def primeFactors(num):
    primes = []
    factorLimit = int(math.sqrt(num)) + 1

    while num % 2 == 0: 
        primes.append(2)
        num = num / 2
    
    for i in range(3, factorLimit, 2):
        while num % i == 0: 
            primes.append(i)
            num = num / i
    
    if num > 2: 
        primes.append(num)
    
    return primes

answer = max(primeFactors(600851475143))
print("The largest prime factor of the number 600851475143 is %s" % answer)
