# LIST IN PYTHON (IT STORE SET OF VALUES )
marks=[78 , 98 , 87 , 67 ,]
print(marks)
#IT CAN STORE ELEMENT OF DIFFERENT TYPES(INT , FLOAT , STRING ETC) 
student=["talish" , 85 , "patna" ]
print(student)
print(type(student))
#LIST IS ALSO MUTABLE THAT MEAN IT CAN CHANGE VALUES ALSO 
student=["talish" , 85 , "patna" ]
student[0] = "mallick"
print(student)
 
#LIST SLICING (SIMILAR TO STRING SLICING ) 

marks = [23 , 45 , 67, 66 ]
print(marks[0:3]) 

#METHOD IN LIST
#list.append() adds one element at thye end 
#list.sort() sort in ascending order
#list.sort(reverse=True) sort in descending order 
#list.reverse() reverse list 
#list.insert(index , element)
#list.copy it copy your list values 
#list.remove() remove first occurence of elemet 
#list.pop(index) remove element at index

marks = [98 , 89 , 66 , 78 , 99]
#marks.append(64) output = [98, 89, 66, 78, 99, 64]
#marks.sort()  output = [66, 78, 89, 98, 99]
#marks.insert(1 ,95)  output =  [98, 95, 89, 66, 78, 99]
#marks.pop(2) output = [98, 89, 78, 99]
print(marks)


# TUPLES IN PYTHON (CREATE IMMUTABLE SEQUENCE OF VALUES)

tup = (1 , 2 , 3 , 4 , 5)
print(tup)
print(type(tup)) # output = (1, 2, 3, 4, 5) , <class 'tuple'>

#METHOD IN TUPLE
#tup.index(element) return index of first occurence 
#tup.count(element) count total occurence

marks = (23 , 43 , 54 , 65)
print(marks.index(54)) # output = 2

print(marks.count(23)) # output = 1

#QUESTION 1. WAP TO ASK USER TO ENTER NAME OF THEIR 3 MOVIES AND STORE THEM IN LIST 

#movie = []
#movie.append(input("enter first movie : "))
#movie.append(input("enter second movie : "))
#movie.append(input("enter third movie : "))

#print(movie) 
#output 
#enter first movie : raid 
#enter second movie : sultan 
#enter third movie : raees
#['raid ', 'sultan ', 'raees']

#QUESTION 2 . WAP TO CHEK IF A LIST CONTAIN A PALINDROME OF ELEMENTS

list= [1 , 2 , 2, 1]
copy_list = list.copy()
copy_list.reverse()
if(copy_list == list):
    print("palindrome")
else:
    print("not palindrome")   # output = palindrome 