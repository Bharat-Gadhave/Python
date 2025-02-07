
my_str = "I Love My India"
vowels = "aeiou"
count = 0

for char in my_str:
    if char.lower() in vowels:
        count +=1
print("Total number of Vowels are  : ",count)