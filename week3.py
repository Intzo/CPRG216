# this is our 3rd class demo
"""
In this class we will work on 
variables, operators and other stuff
"""
#review
#assignemnt
x = 8 #int
y = 1.2 #float
warm = True # bool
msg = "hello" #string of characters
print (x,type(x))
print (y,type(y))
print (warm,type(warm))
print (msg,"type of msg",type(msg))

#some function call : print, input, int,float,str,bool, 
num_as_text = "43"

num_as_num = int(num_as_text)
print (num_as_text,type(num_as_text))
print (num_as_num,type(num_as_num))
print (str(num_as_num)) # equivalent

num = 3
num_f = float(3)
num2 = 3.4
num2_i = int(num2)
num2_as_text = str(num2)

# using input function .. note input function always return a string (text)\

year_of_birth = input("Please Enter your year of birth")
print ("your age is ",2025 -  int(year_of_birth))

#print function 
print ("hello", "world", sep = '', end=' ') #to put 2 lines into 1
print ("hello", "world", sep = '',) #to put words together
print ("hello\tworld") #to put space \t
print ("hello\nworld") #to put 1 line into 2 \n
print ('What is the student\'s name?') #to have apostraphe
print ('Use this symbol\\to make an escape character')# \\ escape character

# precedence rules 

expression = 3+4*0-300+12/3
print (expression) (4/2)*3

# more about Assignment 
# the computer reads right to left example x = 3+4 it will calculate first then assign it to x

x= 3
x = x+5
print(5)
