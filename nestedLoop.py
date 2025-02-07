# Find prime number from given rang 

print("Enter the range i.e numbers First and Second to which find prime numbers between :")
num1 = int(input("Enter The first element : "))
num2 = int(input("Enter The Second element : "))

for num in range(num1,num2):
    for j in range(2,num):
        if num % j == 0:
            break
    else:
        print(num)