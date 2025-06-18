# SET IN PYTHON 
#(SET IS THE COLLECTION OF UNORDERED ITEMS , EACH ELEMENT MUST BE UNIQUE)

num = {1 , 2 , 3, 4}
print(num) 
#you can store (int,flaot,"str",tuple)
num = {2 , 2.34 , "talish" , (23 , 45)}
print(num)  #output ={2, 2.34, 'talish', (23, 45)}

#METHOD IN SET
#1. set.add(element)
#2. set.remove(element)
#3. set.clear()
#4. set.pop()
#5. set.union(set2)
#6. setintersection.(set2)

collection = set()
collection.add(1)
collection.add(2)
print(collection) #this is how you add element in set

name = {"talish", "irfan" , "haider" , "rizwan"}
print(name) #output = {'talish', 'haider', 'rizwan', 'irfan'} in this output will be random

value = {1,2,3,4}
data = {2,4,5,6}
print(value.union(data)) 
#output = {1, 2, 3, 4, 5, 6}

value = {1,2,3,4}
data = {2,4,5,6}
print(value.intersection(data)) #output = {2, 4}

#QUESTION 1. STORE FOLLOWING WORD MEANING IN A PYTHON DICTIONARY
# table : "a piece of furniture" , "list of fact"
# cat : "a small animal"
dict = {
    "table" : ["a piece of furniture" , "list of fact"],
    "cat" : "a small animal"
}
print(dict) #output = {'table': ['a piece of furniture', 'list of fact'], 'cat': 'a small animal'}

#QUESTION 2 . WAP TO ENTER MARKS OF 3 STUDENT FROM THE USER AND STORE THEM IN DICTIONARY.
          #START WITH EMPTY DICT AND ADD ONE BY ONE 
marks = {}
x = int(input("enter phy : "))  
marks.update({"phy" : x})
y = int(input("enter chem : "))  
marks.update({"chem" : x})   
z = int(input("enter math : "))  
marks.update({"math" : x})   
print(marks)  
# output =
#enter phy : 98
#enter chem : 97
#enter math : 99
#{'phy': 98, 'chem': 98, 'math': 98}     