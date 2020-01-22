# problemName = "Largest palindrome product"
# problemNum = 4
# solutionBy = "FIGBERT"
# language = "Python"
# dateCompleted = "21/01/2020"

def palindromeCheck(num):
    reversedNum = int(str(num)[::-1])
    if reversedNum == num:
        return True
    return False

allPossibleCombos = [a*b for a in range(999, 99, -1) for b in range(999, 99, -1) if palindromeCheck(a*b)]
print("The largest palindrome made from the product of two 3-digit numbers is %s" % max(allPossibleCombos))
