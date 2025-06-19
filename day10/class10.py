# WHILW LOOP IN PYTHON (LOOPS ARE REPEAT INSTRUCTION )
#syntax
# while loops
#  while condition
     #some work 

i = 1 
while i <= 5 :
    print("hello" , i)
    i += 1

# 1.print 1 to 10 number in loop 

i = 1 
while i <= 10 :
    print(i)
    i += 1

# 2.print 10 to 1 number in loop

i = 10
while i >= 1:
    print(i)
    i -= 1

# 3.print a table of any number in loop 
n = int(input("enter a number : "))
i =1
while i <=10:
    print(n*i)
    i += 1        

# 4. print the element of the following list using loop
# [1,4,9,16,25,36,49,64,81,100]
nums = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx < len(nums) :
    print(nums[idx])
    idx += 1   

# BREAK AND CONTINUE 
# (BREAK USED TO TERMINATE THE LOOP WHEN ENCOUNTERED)
# (CONTINUE TERMINATE EXECUTION IN THE CURRENT ITERATION AND CONTINUES EXECUTION OF THE LOOP )   

# QUESTION 1 : search for a 49 in this tuple using loop 
#            (1,4,9,16,25,36,49,64,81,100)
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 49
i = 0
while i < len(nums):
    if nums[i] == x:
        print("found at idx", i)
        break
    i += 1

# QUESTION 2 : PRINT ONLY ODD NUMBER IN 1 TO 10 
i = 1 
while i <= 10:
    if(i%2==0):
        i += 1
        continue
    print(i) 
    i += 1       
