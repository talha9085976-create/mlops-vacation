def func(text):
	return len(text)


text = " Cat is an animal with four legs "
length = func(text)
print(length) 

def func(b):
    i=0
    while(i<len(list)):
        print(b[i])
        i+=1


list = [55, 66 , "cat", "dragon", 90 , "Talha"]
a = func(list)



def factorial(n):
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


number = 5
print(factorial(number))

# Test commit for contribution tracking

