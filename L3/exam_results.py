# VERSION 1
# TOTAL 100
# 20 questions 5 poinst 

correct_questions = 3
points = 85

if points >= 80:
    print("Your grade is A")
elif points >= 60:
    print("Your grade is B")
elif points >= 40:
    print("Your grade is C")
elif points >= 20:
    print("Your grade is D")
else:
    print("Your grade is F, You failed")


# VERSION 2

correct_questions = 19
points = 95

if points <= 100 and points >= 80:
    print("Your grade is A")
if points < 80 and points >= 60:
    print("Your grade is B")
if points < 60 and points >= 40:
    print("Your grade is C")
if points < 40 and points >= 20:
    print("Your grade is D")
if points < 20:
    print("Your grade is F, You failed")
