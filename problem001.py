# problemName = "Multiples of 3 and 5"
# problemNum = 1
# solutionBy = "FIGBERT"
# language = "Python"
# dateCompleted = "20/01/2020"

def multOfThreeOrFive(num):
    return num % 3 is 0 or num % 5 is 0

def sumOfMultiplesOfThreeOrFive(num):
    lstOfMults = []
    numStep = num - 1
    while numStep > 0:
        if multOfThreeOrFive(numStep):
            lstOfMults.append(numStep)
        numStep -= 1
    return sum(lstOfMults)

answer = sumOfMultiplesOfThreeOrFive(1000)
print("The sum of all the multiples of 3 or 5 below 1000 is %s" % answer)
