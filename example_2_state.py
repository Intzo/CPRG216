'''print ("welcome to the party")
name = input("Please enter your name")
if name == 'enzo':
    name = 'Enzo'
print ("welcome, ", name )
print ("to have a drink provide age")
age = int(input("what is your age"))

is_adult = age >= 18
if is_adult: #if over 18 it will print this
    print ("you are allowed to drink.")
else: # if false it will print this
    print ("sorry you are not allowed to drink")

# if else works fine if thers only two conditions

print ("welcome to the grade system")
grade = int(input("Please enter your grade"))

if grade >=90:
    letter_grade = 'A'
elif grade>= 80:
    letter_grade = 'B'
elif grade>= 70:
    letter_grade = 'C'
elif grade >=60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print ("your letter grade is", letter_grade)'''

print ("welcome to the quadratic equation solver")
print ("Please enter the three numbers a,b,c")

a = float(input('\n'))
b = float (input('\n'))
c = float (input ('\n'))
x1 = 0
x2 = 0
if a == 0:
    x1 = -b/c
    x2 = -b/c 
else:
    if b**2 >= 4*a*c:
        x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
        x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    else:
        x1 = None
        x2 = None 