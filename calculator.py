def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error! Division by zero"
    return a / b

def avg(a, b):
    return (a + b) / 2

def average(*numbers):
    return sum(numbers) / len(numbers) if numbers else "Error! No numbers provided"

print("\n")
print("!!!!!!!!  Welcome To Bharat's Calculator  !!!!!!!!")
print("\n")
print("Which Operation Would You Like to Perform? (add/sub/mul/div/avg/average)")
print("\n")

select = input("Enter Your Choice: ").strip().lower()

if select in ["add", "sub", "mul", "div", "avg"]:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    
    if select == "add":
        print(f"Sum of {num1} and {num2} is: ", add(num1, num2))
    elif select == "sub":
        print(f"Subtraction of {num1} and {num2} is: ", sub(num1, num2))
    elif select == "mul":
        print(f"Multiplication of {num1} and {num2} is: ", mult(num1, num2))
    elif select == "div":
        print(f"Division of {num1} by {num2} is: ", div(num1, num2))
    elif select == "avg":
        print(f"Average of {num1} and {num2} is: ", avg(num1, num2))
        
elif select == "average":
    numbers = list(map(int, input("Enter numbers separated by space to find average: ").split()))
    print(f"Average of the numbers is: ", average(*numbers))

else:
    print("You Have Entered an Invalid Choice! Goodbye!")

print("Thank You for Using Bharat's Calculator! Have a Great Day! 😊")
