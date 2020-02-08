# problemName = "Sum square difference"
# problemNum = 6
# solutionBy = "FIGBERT"
# language = "Python"
# dateCompleted = "24/01/2020"

if __name__ == "__main__":
    sumOfTheSquares = 0
    squareOfTheSum = 0
    for i in range(1, 101):
        sumOfTheSquares += i**2
        squareOfTheSum += i
    squareOfTheSum = squareOfTheSum**2
    answer = squareOfTheSum - sumOfTheSquares
    print("The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is %s" % answer)
