# problemName = "Highly divisible triangular number"
# problemNum = 12
# solutionBy = "FIGBERT"
# language = "Python"
# dateCompleted = "05/02/2020"
from functools import reduce
from math import sqrt
import time

def moreThanFiveHundredFactors(num):
    factors = len(list(reduce(list.__add__, ([i, num//i] for i in range(1, int(sqrt(num)) + 1) if num % i == 0))))
    return num if factors > 500 else False

def triangle(pos):
    val = 0
    for i in range(1, pos + 1):
        val += i
    return moreThanFiveHundredFactors(val)

answer = 2
while not triangle(answer):
    answer += 1
answer = triangle(answer)
print(f"The value of the first triangle number to have over five hundred divisors is {answer}")
