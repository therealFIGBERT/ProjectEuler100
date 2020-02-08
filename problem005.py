# problemName = "Smallest multiple"
# problemNum = 5
# solutionBy = "FIGBERT"
# language = "Python"
# dateCompleted = "21/01/2020"

if __name__ == "__main__":
    answer = 1
    for i in range(1, 21):
        if answer % i > 0:
            for k in range(1, 21):
                if (answer * k) % i == 0:
                    answer *= k
                    break
    print("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is %s" % answer)
