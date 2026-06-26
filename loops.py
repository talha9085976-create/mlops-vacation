# Simple Loop Examples

# 1. For loop with range
print("For loop 1 to 5:")
for i in range(1, 6):
    print(i)

# 2. For loop with list
print("\nFor loop with list:")
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# 3. While loop
print("\nWhile loop:")
count = 1
while count <= 3:
    print(f"Count: {count}")
    count += 1

# 4. For loop with break
print("\nFor loop with break:")
for i in range(1, 6):
    if i == 3:
        break
    print(i)

# 5. For loop with continue
print("\nFor loop with continue:")
for i in range(1, 6):
    if i == 2:
        continue
    print(i)

# 6. Nested loop
print("\nNested loop (3x3 grid):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i},{j})", end=" ")
    print()

# 7. Sum numbers using loop
print("\nSum 1 to 5:")
total = 0
for num in range(1, 6):
    total += num
print(f"Total: {total}")
