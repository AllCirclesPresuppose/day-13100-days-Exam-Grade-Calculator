print("Exam Grade Calculator")
name = input("What is the Name of your exam? ")
possibleScore = int(input("What is the max possible score? "))
yourScore = int(input("what was your score? "))
percent = round((yourScore / possibleScore) * 100, 2)

if percent == 100:
    score = "A+"
elif percent >= 90:
    score = "A"
elif percent >= 80:
    score = "B"
elif percent >= 70:
    score = "C"
elif percent >= 60:
    score = "D"
else:
    score = "F"

print()
print()
print()
print()
print("\033[33mCalculator Below")
print()
print("Name of exam: \033[32m" + name)
print()
print("\033[33mMax. Possible Score: \033[32m" + str(possibleScore))
print()
print("\033[33mYour score: \033[32m" + str(yourScore))
print()
print("\033[33mYou got " + str(percent) + "% which is a " + score)
