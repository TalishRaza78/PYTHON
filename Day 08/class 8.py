# DICTIONARY IN PYTHON 
# IT STORE DATA VALUES IN KEY.VALUE PAIR 
info = {
    "name" : "talish" ,
    "age" : 18,
    "marks" : (45 , 65 , 67)
    }
# it mutable also
info["name"] = "mallick"
print(info)  #output = {'name': 'mallick', 'age': 18, 'marks': (45, 65, 67)}

# NESTED DICTIONARIES
student = {
    "name"  : "talish" , 
    "subject" : {
        "phy" : 95,
        "chem" : 97 , 
        "math" : 98 
    }
}
print(student) # output = {'name': 'talish', 'subject': {'phy': 95, 'chem': 97, 'math': 98}}

#DICTIONARY METHOD 
#1. myDict.key()
#2. myDict.values()
#3. myDict.items()
#4. myDict.get("key")
#5. myDict.update()
student = {
    "name"  : "talish" , 
    "subject" : {
        "phy" : 95,
        "chem" : 97 , 
        "math" : 98 
        }
}
print(student.keys()) #output = dict_keys(['name', 'subject'])
print(student.values()) #output = dict_values(['talish', {'phy': 95, 'chem': 97, 'math': 98}])
print(student.items()) #output = dict_items([('name', 'talish'), ('subject', {'phy': 95, 'chem': 97, 'math': 98})])
print(student.get("name")) #output = talish
student.update({"city" : "patna"})
print(student) # this method add the above key and values in your student dictionary
#output = {'name': 'talish', 'subject': {'phy': 95, 'chem': 97, 'math': 98}, 'city': 'patna'}