# problemName = "Summation of primes"
# problemNum = 10
# solutionBy = "FIGBERT"
# language = "Python"
# dateCompleted = "28/01/2020"

def sieveOfEratosthenes(limit):
    prime = [True for _ in range(limit+1)]
    p = 2
    while (p * p <= limit): 
        if (prime[p] == True): 
            for i in range(p * 2, limit + 1, p): 
                prime[i] = False
        p += 1
    prime[0:2] = [False, False]
    return [p for p in range(limit + 1) if prime[p]]

if __name__ == "__main__":
    primes = sieveOfEratosthenes(2000000)
    print(f"The sum of all the primes below two million is {sum(primes)}")
