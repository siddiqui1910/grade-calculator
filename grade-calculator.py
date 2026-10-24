#Grade Calculator

#taking input and making sure that values stay under 100
a = float(input("Enter the marks of English out of 100: "))
if(a>100 or a<0):
    print("Please Enter a Valid Value")
    exit()   
b = float(input("Enter the marks of Maths out of 100: "))
if(b>100 or b<0):
    print("Please Enter a Valid Value")
    exit()    
c = float(input("Enter the marks of Physics out of 100: "))
if(c>100 or c<0):
    print("Please Enter a Valid Value")
    exit()   
d = float(input("Enter the marks of Computer out of 100: "))
if(d>100 or d<0):
    print("Please Enter a Valid Value")
    exit()    

#Calculations
total_marks = 400.00
obtained_marks = a + b + c + d #No need to apply any check here as the value must be correc to have passed the upper input taking section
percent = (obtained_marks/total_marks) * 100

#Conditions
if(percent >= 90 and percent <= 100):
    print("Your percentage is ", percent, " and your grade is A!")
elif(percent >= 80 and percent < 90):
    print("Your percentage is ", percent, " and your grade is B!")
elif(percent >= 70 and percent < 80):
    print("Your percentage is ", percent, " and your grade is C!")
elif(percent >= 60 and percent < 70):
    print("Your percentage is ", percent, " and your grade is D!")
else:
    print("Your percentage is ", percent, " and your grade is F!")