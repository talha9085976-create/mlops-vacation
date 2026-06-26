
str1 = 'PAKISTAN'
num=34.44
Marks=["Talha",23.5,24,33,44,'APNA',str1,num]
print(Marks)
print(Marks[6])

Marks.append('ISLAMABAD')
print(Marks)
num2=[44,55,77,32,45,65]

print(Marks)
num2.sort()
print(num2)
num2.sort(reverse=True)
print(num2)



num3=[44,55,77,32,45,65]
num3.reverse()
print(num3)



str2=[ 'a','v ','g', 'e ', 'k', 'l', 'm', 'n', 'o', 'p']
str2.insert(1,'k')
print(str2)
  
str2.remove("p")
print(str2)
num3.pop(2)
print(num3)


mov1 = str(input("Enter your first movie name: "))
mov2 = str(input("Enter your second movie name: "))
movies =[mov1, mov2]
print(movies)


list1 = list(input("Enter your list items separated by space: ").split())
copy_list = list1.copy()
list1.reverse()
if list1== copy_list:
    print("The list is palindrome")
else:
    print("The list is not palindrome")