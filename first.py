# # vr = '''Pythin is a fun.\n"Quotes" and 'single quotes' can be tricky'''
# # print(vr)


# name = "Bharat Gadhave"
# age = 26;
# city = "Pune"
# print( f"Hi my name is {name} and my age is {age} and I belongs to city {city}")

# name = input()

# print("Hello "+ name + "How are You ? ")
# =================================================================
# number1 = input("Insert first number : ")
# number2 = input("insert Second number: ")

# print("Addition of Two numbers is = ", int(number1)+int(number2))
# ========================================================================

# name = input("Enter name of student : ")
# marks = input(f"Enter marks of student {name} : ")
# # dict = {"name" : name,
# #         "Marks" : marks}
# # print(dict)
# print(f"Student Name : {name} \nStudent Marks : {marks}")
# =============================================================================
# WAP to inpute student name and marks of three subjects . print name and percentage in outeput

# name = input("Enter name of student : ")
# s1,s2,s3 = input("Enter Mark of first sunjest : "),input("Enter Mark of Second sunjest : "),input("Enter Mark of Third sunjest : ")
# percentage = ((int(s1)+int(s2)+int(s3))/300)*100
# print(f"name : {name} \n Pecentage : {percentage}") 

# ====================================================================================

# WAP to store inpute data of student in dictionery
# print("!!!!!!!! Student Information !!!!!!!!")
# student_data = {}

# student_data['name'] = input("Enter student Name : ")
# student_data['Age'] = int(input("Enter age of srudent : "))
# student_data['Hight'] = float(input("Enter Hight of Student : "))
# student_data['Student Status'] = input("Are you a student Yes/No : ")

# print(student_data)
# ====================================================================================

# temperature = int(input("Enter Today's Temperature : "))
# if temperature > 20:
#         print("Today is hot day")
# else:
#     print("Taday is Cool day")

# ======================================================================================

# number = int(input("Enter The number"))

# if number > 0:
#     if number%2 == 0:
#         print("Number is positive and even")
#     else:
#         print("Nuber is positive ans odd")
# else:
#     if number == 0:
#         print("Number is Zero")
#     else:
#         print("Number is Negative.")

# =========================Assignment===============================
# value = None
# if value:
#     print("value is true")
# else:
#     print("Value is false")

# ============================================assesments==============================

# year = int(input("Enter Year to Check Wether it is Leap year Or not : "))

# def is_leap_year(year):
#     if(year%4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     return False

# if is_leap_year(year):
#     print(f"{year} year is Leap year")
# else:
#     print(f"{year} Year is not Leap Year")

# =======================================================Assignment3===============================

# username = "bharat@gmail.com"
# password = "Bharat@123"

# user = input("Enter Username of user to login : ")
# pwd = input("Enter Password of user to login : ")

# if(user == username and pwd == password):
#     print("Both Username And Passwod Are correct.")
#     print("Well come Home !!!!!!")
# elif(user == username and pwd !=password):
#     print("Password is Incorrect!")
# else:
#     print("Username is InCorrect")

# if(user == username):
#     if(pwd == password):
#         print("Both Username and password are correct ...")
#         print("WelCome to HomePage!!!!!!")
#     else:
#         print("Passwod is Incorrect.")
# else:
#     print("Username is incorect.")

# ================================================================================================?
# Check Eligibility of student to take admition in college.
# conditions : 
# marks is mathematicks >= 65
# marks is physics >= 55
# marks is chemestry >= 50
# total marks in all three subject >=180 marks or total marks in mathematicks and physics >= 140

# print("Enter PCM marks out Of 100")
# math_marks = int(input("Enter marks of Maths : "))
# physics_marks = int(input("Enter marks of physics : "))
# chemitry_marks = int(input("Enter marks of chemistry : "))


# total_marks_of_all_three_subjects = math_marks + physics_marks + chemitry_marks
# total_marks_of_physics_and_maths = math_marks + physics_marks

# if(math_marks >= 65 and physics_marks >=55 and chemitry_marks >= 50):
#     if(total_marks_of_all_three_subjects >= 180 or total_marks_of_physics_and_maths >= 140):
#         print("\n")
#         print("Congratulations !!!!!!!!")
#         print("Student is Eligible to take admission in College.")
#     else:
#         print("\n")
#         print("Unfortunately Student is not Eligible to take admission inThis College ")
#         print(f"Total marks in All three subjects is : {total_marks_of_all_three_subjects}")
#         print(f"Total marks in Physics and Chemistry subjects is : {total_marks_of_physics_and_maths}")
# else:
#     print("\n")
#     print("Unfortunately Student is not Eligible to take admission inThis College")
#     print("student marks are not satisefied....")
#     print(f"Maths_Marks >= 65 physics_marks >=55 and chemitry_marks >= 50 \nBut you got Marks Of :  \n    physics_marks = {physics_marks}\n    chemitry_marks = {chemitry_marks}\n    math_marks = {math_marks}\n")


# ========================================Functions==============================
# def addTwoNumbers(a,b):
#     result = a + b
#     print("Addition of two numbers is : ",result)


# addTwoNumbers(5,10)
# ========================================================================================

# create a function to calculate/convert celcius into farenhight

def celcius_to_fahrenhight(celcius):
    fehrenhight = (celcius * 9/5) + 32
    return fehrenhight

result = celcius_to_fahrenhight(25)
print(result) 























