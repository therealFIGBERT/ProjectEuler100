# problemName = "Sum square difference"
# problemNum = 6
# solutionBy = "FIGBERT"
# language = "Python"
# dateCompleted = "24/01/2020"

if __name__ == "__main__":
    sum_of_the_squares = 0
    square_of_the_sum = 0
    for i in range(1, 101):
        sum_of_the_squares += i**2
        square_of_the_sum += i
    square_of_the_sum = square_of_the_sum**2
    answer = square_of_the_sum - sum_of_the_squares
    print((
        "The difference between the sum of the squares of the first one "
        "hundred natural numbers and the square of the sum is %s" % answer
    ))
