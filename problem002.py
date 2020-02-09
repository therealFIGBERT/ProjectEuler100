# problemName = "Even Fibonacci numbers"
# problemNum = 2
# solutionBy = "FIGBERT"
# language = "Python"
# dateCompleted = "20/01/2020"

def fibonacci(limit):
    list_ = [1,2]
    while list_[-1] <= limit:
        list_.append(list_[-2] + list_[-1])
    return list_

def sum_of_evens_in_list(src_list):
    list_ = []
    for i in src_list:
        if i % 2 == 0:
            list_.append(i)
    return sum(list_)

if __name__ == "__main__":
    fibonacci_until_4_mil = fibonacci(4000000)
    answer = sum_of_evens_in_list(fibonacci_until_4_mil)
    print((
        "By considering the terms in the Fibonacci sequence whose values do "
        "not exceed four million, the sum of the even-valued terms is "
        "{}".format(answer)
    ))
