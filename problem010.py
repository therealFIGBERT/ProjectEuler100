# problemName = "Summation of primes"
# problemNum = 10
# solutionBy = "FIGBERT"
# language = "Python"
# dateCompleted = "28/01/2020"

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
    primes = sieve_of_eratosthenes(2000000)
    print(f"The sum of all the primes below two million is {sum(primes)}")
