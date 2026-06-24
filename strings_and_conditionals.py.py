str1 ="cat is an animal"
len(str1)
print(len(str1))
print(str1[1:9])
str2 = "dog is also an animal"
print (str2[-5:])
print(str1.endswith("animal"))
print(str2.endswith("dog"))
print(str1.replace('cat','lion'))
print(str2.replace('dog','wolf'))
print(str1.capitalize())
print(str2.capitalize())
print(str1.find("a"))
print(str2.find("g"))
print(str2.count("a"))
print(str1.count("i"))

a = str(input("Enter your name: "))
print(len(a))

str45= "Hello, $hanty How are you?   ,  you are home $hanty and you are good $hanty $$$$$$$$$$$"
print(str45.count("$"))




print("Enter your Marks")
Marks = int(input())
if(Marks >= 90 and Marks <= 100):
    print("A+")
elif(Marks >= 80 and Marks < 90):
    print("A")
elif(Marks >= 70 and Marks < 80):
    print("B")
else:
    print("Fail")


print("Enter your number")
number = int(input())
if (number%7==0):
    print("Divisible by 7")
else:
    print("Not Divisible by 7")

