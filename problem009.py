# problemName = "Special Pythagorean triplet"
# problemNum = 9
# solutionBy = "FIGBERT"
# language = "Python"
# dateCompleted = "28/01/2020"
from math import sqrt

def triplet(a, b):
    c = sqrt(a**2 + b**2)
    if a + b + c == 1000:
        return int(a*b*c)
    return False

if __name__ == "__main__":
    for (i, k) in [(a, b) for a in range(500) for b in range(500) if a < b]:
        answer = triplet(i, k)
        if answer:
            print(f"The product of abc, where:\n\ta < b < c,\n\ta2 + b2 = c2,\n\ta + b + c = 1000\nis {answer}")
