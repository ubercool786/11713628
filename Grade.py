#Display Grade
marks=float(input("Enter Marks: "))
if(marks>=90):
    print("Grade is O")
elif(marks>=80 and marks<90):
    print("Grade is A+")
elif(marks>=70 and marks<80):
    print("Grade is A")
elif(marks>=60 and marks<70):
    print("Grade is B+")
elif(marks>=50 and marks<60):
    print("Grade is B")
elif(marks>=40 and marks<50):
    print("Grade is C")
else:
    print("Fail")
