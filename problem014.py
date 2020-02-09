# problemName = "Longest Collatz sequence"
# problemNum = 14
# solutionBy = "FIGBERT"
# language = "Python"
# dateCompleted = "06/02/2020"

def collatz(num):
    sequence = 1
    while num > 1:
        if num % 2 == 0:
            num = num//2
        else:
            num = (3*num) + 1
        sequence += 1
    return sequence

if __name__ == "__main__":
    answer = [999999, 999999, collatz(999999)]
    while answer[0] >= 1:
        potential = (answer[0] - 1, collatz(answer[0] - 1))
        if potential[1] > answer[2]:
            answer[1] = potential[0]
            answer[2] = potential[1]
        answer[0] = answer[0] - 1
    print((
        "The starting number, under one million, that produces the "
        f"longest chain from the given iterative sequence is {answer[1]}"
    ))
