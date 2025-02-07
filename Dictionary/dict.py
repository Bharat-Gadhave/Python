# Mathod 1

# cources = {"Name": "Python",
#             "Instructor": "Bharat Gadhave",
#             "Level": "Biginner"}

# print(cources)
# print(type(cources))


# Method 2

# parson = dict(name = "Bharat Gadhave",age = 26, grade = "A")
# print(parson)
# print(type(parson))

# Method 3
# parson = dict([('name','Bharat G'),('age',20),('grade','A')])
# print(parson)
# print(type(parson))



# How to access values of dict

# print(parson['name'])

# print(parson['age'])
# ===================



# Nested Dictonary

student = {
    "student1" : {
            id : 1,
            "name" : "Sharad G",
            "age" : 25,
            "College Name": "Fegusson College pune",
            "email":"sharadgadhave777@gmail.com"},

    "student2" : {
        id : 2,
        "name" : "Anjali G",
        "age" : 23,
        "College Name": "Fegusson College pune",
        "email":"anjaligadhave777@gmail.com"},

    "student3" :{
        id : 3,
        "name" : "Chhaya G",
        "age" : 27,
        "College Name": "Fegusson College pune",
        "email":"chhayagadhave777@gmail.com"},

    "student4" : {
        id : 4,
        "name" : "Sushila G",
        "age" : 30,
        "College Name": "Deogiri College Chatrapati Sambhajinagar",
        "email":"sushilagadhave777@gmail.com"},

    "student5" : {
        id : 5,
        "name" : "Punjaram Gadhave",
        "age" : 45,
        "College Name": "Fegusson College pune",
        "email":"punjaramgadhave777@gmail.com"}
    }

# print(student["student5"]["name"])
# print((student.keys()))

# for keys,values in student.items():
#     print(keys, values)
# Dictonary Methods 

# add, remove, modify
# To add data in dict
# student["student5"]["Phone Number"] = "9403501264"
# print(student["student5"])

# To Modify data in dict
# student["student5"]["age"] = 16
# print(student["student5"])

# to remove data from dict : we can use "del" or .pop()
# del student["student5"]["Phone Number"]
# print(student["student5"])

# =====================================
# Dictionary Comprihentions

# syntax 
# new_dict = {key_expression:value_exp for item in iterable if condition}
# my_dict = {x:x*x for x in range(1,11) if x%2==0}

# print(my_dict)