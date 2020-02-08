# problemName = "Largest palindrome product"
# problemNum = 4
# solutionBy = "FIGBERT"
# language = "Python"
# dateCompleted = "21/01/2020"

if __name__ == "__main__":
    allPossibleCombos = [a*b for a in range(999, 99, -1) for b in range(999, 99, -1) if int(str(a*b)[::-1]) == a*b]
    print("The largest palindrome made from the product of two 3-digit numbers is %s" % max(allPossibleCombos))
