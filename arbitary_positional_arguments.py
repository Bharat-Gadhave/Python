# Arbitory Arguments

# Arbitory Positional Arguments (*args)
# Note : Stores arguments as tuple


# =======================Example1======================
def addNumbers(*numbers):
    # print(type(numbers)) #Stores arguments as tuple
    return sum(numbers)

# print(addNumbers(4 ,5, 6))
result = addNumbers(4,5,6)
print(result)

# =======================Example2======================

def greetings(*names):
    for name in names:
        print(f"Hello {name} !")

greetings("Bharat","Sharad","Anjali","Chhaya")


# =======================Example3======================
# to find average of given numbers
def avgOfGivenNumbers(*numbers):
    return sum(numbers)/len(numbers)

result = avgOfGivenNumbers(1,2,3,4,5,6,7,8,9)
print(result)

## Arbitary Keyword Arguments (**KWargs)
# Note : stores argument as dictionary
# ==================================Example of Keyword Arguments=======================
def studentInfo(**info):
    # print(type(info)) # dictionary type :  <class 'dict'>
    for key,value in info.items():
        print(f"{key} : {value}")

studentInfo(name = "Bharat Gadhave", Age = 26, Address = "Narhe,Pune" , collageName = "Fergussion College Pune"
            )