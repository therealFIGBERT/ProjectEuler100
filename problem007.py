# problemName = "10001st prime"
# problemNum = 7
# solutionBy = "FIGBERT"
# language = "Python"
# dateCompleted = "24/01/2020"
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
import math

def sieveOfEratosthenes(limit):
    prime = [True for _ in range(limit+1)]
    p = 2
    while (p * p <= limit): 
        if (prime[p] == True): 
            for i in range(p * 2, limit+ 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    return [p for p in range(limit + 1) if prime[p]]

def search():
    searchRange = 100
    returnValue = sieveOfEratosthenes(searchRange)
    while len(returnValue) < 10001:
        searchRange += 100
        returnValue = sieveOfEratosthenes(searchRange)
    print(returnValue[10000])

search()