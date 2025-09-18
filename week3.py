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

