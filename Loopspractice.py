

#WHILE LOOP PRACTICE
i = 1 
while i <= 1:
    print(i)
    i += 1


j = 1 
while j != 10:
    print(j)    
    j += 1

i=1
while i <=100:
    print(i)
    i += 1

i = 100
while i>=0 :
    print(i)
    i-=1


n = int(input("Enter a number "))
i = 1
while i <= 10:
    print(n * i)
    i += 1


list = [ 1 , 4 ,9 ,16 ,25 ,36 ,49 ,64 ,81 ]
i = 0
while i <= 8 :
    print ( list[i])
    i+=1


numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81]
x = int(input("Enter an index number you want to find: "))
i = 0

while i <= 8:
    if i == x:
        print(numbers[i])
    i += 1 

#FOR LOOP  PRACTICE

numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81]

for value in numbers:
    print(value)




numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81]
x=int(input("Enter a number u want to find :"))
index=0
for i in numbers:
    if i==x:
      print(index)
    index+=1 


for i in range(0 , 100 , 4):
     print(i)

numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81]
x = 81
for i in numbers :
     if(x==i):
      print(i)



# Step 1: Take input from the user (separated by spaces)
user_input = input("Enter numbers separated by spaces: ")

# Step 2: Split the string by spaces and convert it into a tuple of strings
string_tuple = tuple(user_input.split())

# Step 3: Initialize variables for the while loop
total_sum = 0
index = 0

# Step 4: Use a while loop to iterate and add numbers
while index < len(string_tuple):
    # We must convert each item from a string to an integer/float before adding
    total_sum += float(string_tuple[index])
    index += 1  # Increment the index to avoid an infinite loop

# Step 5: Print the final sum
print("The sum of your tuple is:", total_sum)

# 1. Ask the user for a number
num = int(input("Enter a number to find its factorial: "))

# 2. Initialize the factorial variable to 1
factorial = 1

# 3. Check if the number is negative, zero, or positive
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    # Loop from 1 up to (num + 1) because range() excludes the stop number
    for i in range(1, num + 1):
        factorial *= i  # This is short for: factorial = factorial * i

    print(f"The factorial of {num} is: {factorial}")