#types of operator
 
#1. arithmetic operators(+,-,*,/,%,**)
a=5
b=4
print(a+b)  
print(a-b)
print(a*b)
print(a/b)
print(a%b) #remainder 
print(a**b) #a to the power b

#2. relational operator(==,!=,>,<,>=,<=)
a=50
b=20
print(a==b) #false
print(a!=b) #true
print(a>b) #true
print(a<b) #false 

#3. assignment operator(+=,-=,*=,/=,%=,**=)
num = 10 
num += 5 #same for sub(-=), mul(*=), div(/=), modulas(%=), power(**=) 
print("num:",num)

x= 12
x-= 10
print("x:" , x)

#4. logical operator (not , and , or)
a=50
b=30
print(not(a>b)) #work on single operand 
print(not(a<b))

val1=True #work on two value and give true answer when both val is true 
val2=True 
print("and operator:",a>b and a>=b) 

val1=True #work on two value and give true answer when atleast one value is true 
val2=False 
print("or operator:",a==b or a>b)


