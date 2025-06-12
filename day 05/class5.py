#STRING (string is data type that store a sequence of character) :
 
#basic operation 
#1. concatenation 
str1 = "hello"
str2 = "pyhton"
final_str=str1+str2
print (final_str) # output(hellopython)

#2.length of str 
str1 = "hello"
print(len(str1))
str2 = "pyhton"
print(len(str2))
print (str1+str2) # output(5 , 6 , hellopyhton)

#3. indexing 
str="i am talish raza mallick "
print(str[7]) # output(l)

#4. slicing 
str = "my name is talish raza mallick"
print(str[1:6]) #output (y nam)

#STRING FUNCTION 
str = "i am studying python"
#now take one by one function 

print(str.endswith("on")) # output (True)

print(str.capitalize()) #output (I am studying python)

print(str.replace("t" , "a")) #output (i am saudying pyahon)

print(str.find("d")) #output (8 , you can search word also )

print(str.count("y")) #output (2 , 2 times y use in this sentence )

#QUESTION 1. WAP to input uses's name amd print its lenght 

name=input("enter your name :")
print("the length is", len(name)) # output (enter your name :talish , the length is 6)
