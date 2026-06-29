# ===== FILE WRITING =====
print("===== FILE WRITING =====")
f = open("data.txt", "a")
content = ". I am learning python since 2020."
f.write(content)
print("Written to file:", content)
f.close()

# ===== FILE READING - read() method =====
print("\n===== FILE READING - read() method =====")
with open("data.txt", "r") as f:
    file_data = f.read()
    print("Full file content:")
    print(file_data)

# ===== FILE READING - readline() method =====
print("\n===== FILE READING - readline() method =====")
with open("data.txt", "r") as f:
    line1 = f.readline()
    print("First line:", line1.strip())
    line2 = f.readline()
    if line2:
        print("Second line:", line2.strip())
    else:
        print("No second line")

# ===== FILE READING - readlines() method =====
print("\n===== FILE READING - readlines() method =====")
with open("data.txt", "r") as f:
    lines = f.readlines()
    print(f"Total lines: {len(lines)}")
    for i, line in enumerate(lines, 1):
        print(f"Line {i}: {line.strip()}")

# ===== USER INPUT =====
print("\n===== USER INPUT =====")
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello {name}, you are {age} years old")

# ===== WRITING MULTIPLE LINES =====
print("\n===== WRITING MULTIPLE LINES =====")
lines_to_write = ["Line 1: Python basics\n", "Line 2: File I/O\n", "Line 3: Functions\n"]
with open("data.txt", "w") as f:  # "w" mode overwrites the file
    f.writelines(lines_to_write)
print("Multiple lines written")

# ===== READ AND DISPLAY =====
print("\n===== FINAL FILE CONTENT =====")
with open("data.txt", "r") as f:
    print(f.read())