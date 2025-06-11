#type conversion 
# 1. conversion -automatically  
# 2. casting - manual 

a = 2
b = 4.25
sum = a+b
print ("sum:", sum )
 
#casting means change the data type manually
#eg:
a = 5
#b = "10" #(it cant run becoz str + int , thats whys change we change the data type by using casting )
b = int("10")
print(type(b)) #check type b  
print (a+b)

#INPUT IN PYTHON 

name = input("enter your name ") #(this is how input work in python)
print("welcome" ,name )

#if you want to check the data type which you enter in your terminal 
name = input("enter your name :")
print(type(name)) 

#take one example after you understand clearly

name = input("enter your name :")
age = int(input("enter your age :"))  #(this will tell you your age is integer value )
marks = float(input("enter your marks:")) #(this will tell you your is float value)
print("welcome", name)
print("age=",age )
print("marks=", marks) 
 
print(type(name))
print(type(age))
print(type(marks))

# this how your output show 

#enter your name :talish
#enter your age :21
#enter your marks:87
#welcome talish
#age= 21
#marks= 87.0
#<class 'str'>
#<class 'int'>
#<class 'float'>