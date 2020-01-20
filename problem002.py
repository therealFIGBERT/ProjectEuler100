# problemName = "Even Fibonacci numbers"
# problemNum = 2
# solutionBy = "FIGBERT"
# language = "Python"
# dateCompleted = "20/01/2020"

def fib(limit):
    lst = [1,2]
    while lst[-1] <= limit:
        lst.append(lst[-2] + lst[-1])
    return lst

def sumOfEvensInList(srcList):
    lst = []
    for i in srcList:
        if i % 2 == 0:
            lst.append(i)
    return sum(lst)

fibUntil4Mil = fib(4000000)
answer = sumOfEvensInList(fibUntil4Mil)
print((
    "By considering the terms in the Fibonacci sequence whose values do not "
    "exceed four million, the sum of the even-valued terms is {}".format(answer)
))
