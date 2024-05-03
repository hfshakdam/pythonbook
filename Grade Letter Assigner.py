#student_score = int(input("What score did you get in your test? "))

'''if student_grade >= 90:
    print("Congratulations! You got an A")
elif student_grade >= 80 and student_grade < 90:
    print("Great! You got a B")
elif student_grade >= 70 and student_grade < 80:
    print("Good work! You got a C")
elif student_grade >= 60 and student_grade < 70:
    print("You got a d")
else:
    print("wtf bro you got an F? pattern up smh")'''
#The above code is very inefficient, here's how to write it better

student_score = int(input("What score did you get in your test? "))

if student_score >= 90:
    grade = "A"
elif student_score >= 80:
    grade = "B"
elif student_score >= 70:
    grade = "C"
elif student_score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your score was {student_score} and that got you a grade {grade}")