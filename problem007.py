# problemName = "10001st prime"
# problemNum = 7
# solutionBy = "FIGBERT"
# language = "Python"
# dateCompleted = "24/01/2020"

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
    searchRange = 1000
    returnValue = sieveOfEratosthenes(searchRange)
    while len(returnValue) < 10001:
        searchRange += 1000
        returnValue = sieveOfEratosthenes(searchRange)
    print("The 10,001st prime number is %s" % returnValue[10000])
