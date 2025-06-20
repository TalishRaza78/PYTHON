# FOR LOOP IN PYTHON 
# USED FOR SEQUENCE TRAVERSAL . FOR TRAVERSING LIST , STRING , TUPLES ETC 
list = [1 , 2 , 3, 4 , 5]
for val in list :
     print(val)
# # same as string 
str = ("talish raza") 
for char in str:
     print(char) 

nums = (1 , 4, 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100)
x =49
idx = 0
for val in nums:
     if(val == x):
         print("found at idx " , idx) 
     idx += 1   

#  RANGE IN LOOP 
#  IT RETURN A SEQUENCE OF NUMBER 
#  RANGE (START , STOP , STEP)
for val in range(1 , 5):
     print(val)      

# QUESTION : PRINT EVEN NUMBER IN 1 TO 100
for num in range(2, 101 , 2):
     print(num)

# QUESTION : PRINT THE MULTIPLICATION OF A NUMBER N 
n = int(input("enter a number"))    
for i in range(1 ,11):
     print(n*i)

# QUESTION : WAP TO FIND THE SUM OF FIRST N NUMBER (USING BOTH WHILE AND FOR ) 

# WHILE LOOP 
n = int(input("enter a number : "))
sum = 0
i = 1
while i <= n :
     sum += i
     i += 1
print("total sum = ", sum )  

# FOR LOOP 
n = int(input("enter a number "))
sum = 0 
for i in range(1 , n+1):
     sum += i
print("sum = ", sum )  

#QUESTION : WAP TO FIND THR FACTORIAL OF FIRST N NUMBER (WHILE AND FOR )

# WHILE LOOP 
n = int(input("enter a number "))
fact = 1 
i = 1
while i <= n :
    fact *= i
    i += 1
print("factorial =", fact )   

# FOR LOOP 
n = int(input("enter a number "))
fact = 1
for i in range(1 , n+1):
       fact *= i
print("factorial =", fact ) 



      