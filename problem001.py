# problemName = "Multiples of 3 and 5"
# problemNum = 1
# solutionBy = "FIGBERT"
# language = "Python"
# dateCompleted = "20/01/2020"

def mult_of_three_or_five(num):
    return num % 3 == 0 or num % 5 == 0

def sum_of_multiples_of_three_or_five(num):
    list_of_multiples = []
    num_step = num - 1
    while num_step > 0:
        if mult_of_three_or_five(num_step):
            list_of_multiples.append(num_step)
        num_step -= 1
    return sum(list_of_multiples)

if __name__ == "__main__":
    answer = sum_of_multiples_of_three_or_five(1000)
    print("The sum of all the multiples of 3 or 5 below 1000 is %s" % answer)
