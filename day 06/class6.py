# CONDITIONAL STATEMENT 
#if
#elif
#else 

age =19
if(age>=18):
    print("can drive") #the space before we write print is compulsary and is called identation

    #lets take another eg where we use elif and else statement
light = "yellow" 
if (light == "green"):
    print("go")
elif (light == "red"):
    print("stop")
elif (light == "yellow"):
    print("look")
else:
    print("the traffic light is broken") #output = look 

    #Grade students based on marks

#marks >= 90, grade =“A”

#90 > marks >= 80, grade =“B”

#80 > marks >= 70, grade =“C”

#70 > marks , grade="D"

marks = int(input("enter your marks: "))

if(marks>=90):
    grade = "A"
elif(marks>=80 and marks < 90):
    grade = "B"
elif(marks>=70 and marks < 80):
    grade = "C"
else:
    grade = "D" 
print("grade of the student : ", grade)  #output = enter your marks: 76 ,grade of the student :  C

# QUESTION: WAP TO CHECK IF A NUMBER ENTERED BY THE USER IS ODD OR EVEN 
  
num = int(input("Enter a number: "))

if (num % 2 == 0):
    print("even.")
else:
    print(" odd.")   #OUTPUT = ENTER A NUMBER 24 , EVEN 

