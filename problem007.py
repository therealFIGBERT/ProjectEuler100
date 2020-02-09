# problemName = "10001st prime"
# problemNum = 7
# solutionBy = "FIGBERT"
# language = "Python"
# dateCompleted = "24/01/2020"

def sieve_of_eratosthenes(limit):
    prime = [True for _ in range(limit+1)]
    prime_pos = 2
    while (prime_pos**2 <= limit): 
        if (prime[prime_pos] == True): 
            for i in range(prime_pos * 2, limit + 1, prime_pos): 
                prime[i] = False
        prime_pos += 1
    prime[0:2] = [False, False]
    return [prime_pos for prime_pos in range(limit + 1) if prime[prime_pos]]

if __name__ == "__main__":
    search_range = 1000
    return_value = sieve_of_eratosthenes(search_range)
    while len(return_value) < 10001:
        search_range += 1000
        return_value = sieve_of_eratosthenes(search_range)
    print("The 10,001st prime number is %s" % return_value[10000])
