# 📌 What is CLI?
# CLI (Command-Line Interface) is a way to interact with a computer program by typing text commands instead of using a graphical user interface (GUI).
# ✅ CLI applications run in terminals like Command Prompt, PowerShell, Terminal, or Bash.
# ✅ They are lightweight, efficient, and widely used in scripting and automation.



# 2️⃣ Python Syntax, Variables & Data Types
# print("Hello, World!")

# def greetUser():

name = "Alice" # String
age = 25  #Integer
height = 5.3   # Float
is_student = True  # Boolean

# print(age)
# print(height)
# print(is_student)

# print(type(name))
# print(type(age))
# print(type(is_student))

# 3️⃣ Conditional Statements (if, elif, else)
# age = 17
# if age >= 18:
#     print("User is allowed to proceed")
# elif age == 17:
#     print("Wait one more year!")
# else:
#     print("You are not Allowed here")



# 4️⃣ Loops (for, while)
# for count in range(2, 15, 3):
#     print(count)

# count = -4
# while count <= 5:
#     print(count)
#     count += 1




# 5️⃣ Functions & Scope
def greet(name): # def keyword, function name and a parameter
    return f"Hello, {name}"  # return statement

# Calling greet() function
# print(greet("John Doe"))
# print(greet("Alice Doe"))
# print(greet("Smith Doe"))
# print(greet("Jack Doe"))

# Scope
# Local Scope → Inside a function
# def show():
#     local_var = "I'm a local guy"
#     print(local_var)

# print(show())
# print(local_var)
# Global Scope → Outside functions

global_var = "I'm a global guy men!"
def show():
    print(global_var)

# print(show())

# 6️⃣ Lists, Tuples, Sets, and Dictionaries
# List ordered, mutable
fruit = [  "Banana", "Apple", "Mango", "Cherry" ]
# print("First List",fruit)
fruit.append("Orange")
# print("Added orange to List",fruit)
sorted_list = fruit.sort()
# print("Sorted List: ", fruit)

# Tuple
coordinate = (10, 20)
# print(coordinate)
# print(coordinate[0])
# print(coordinate[1])

# Set
colors = {"red", "green", "blue"}
colors.add("Yellow")
# print(colors)

# Dictionaries
person = {"name": "Alice", "age": 25}
# print(person["name"])
# print(person["age"])
# print(person)

# 7️⃣ Exception Handling (try-except)
# try:
#     num = int(input("Enter a number: "))
#     print(10 / num)

# except ValueError:
#     print("Please enter a number")
# except ZeroDivisionError:
#     print("Cannot divide by Zero")
# finally:
#     print("Execution Completed")



# 8️⃣ Basic File Handling (open, read, write)
with open("file.docx", "w") as file:
    file.write("Hello World, Heelo World\n, Hello Worl")

with open("file.docx", "r") as file:
    content = file.read()
    print(content)

# 🛠 Project: To-Do List (CLI App)