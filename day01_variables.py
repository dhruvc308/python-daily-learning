# Day 1: Python Variables

# 1. Basic Variable Declaration andusing print() function

name = "Dhruv"
age = 23
height = 5.9
is_male = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Male:", is_male)



# 2. Checking Data Types using type() function

print("\n--- Data Types ---")
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))



# 3. Multiple Variable Assignment in single statement

a, b, c = 10, 20, 30
print("\nMultiple Assignment:")
print("a =", a, "b =", b, "c =", c)


# Same value to multiple variables
x = y = z = 100
print("\nSame Value Assignment:")
print("x =", x, "y =", y, "z =", z)



# 4. Changing Variable Values

score = 50
print("\nInitial Score:", score)

score = 75
print("Updated Score:", score)



# 5. Type Casting

num = "25"
print("\nBefore Type Casting:", num, type(num))

num = int(num)
print("After Type Casting:", num, type(num))



# 6. Taking User Input using input() function

print("\n--- User Input ---")
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print("Hello", user_name)
print("You are", user_age, "years old")



# 7. Simple Variable Operations

num1 = 10
num2 = 5

print("\n--- Operations ---")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)



# 8. Variable Swapping (Method 1)

a = 5
b = 10

print("\nBefore Swapping (Method 1): a =", a, "b =", b)

temp = a
a = b
b = temp

print("After Swapping (Method 1): a =", a, "b =", b)



# 9. Variable Swapping (Method 2)

x = 15
y = 25

print("\nBefore Swapping (Method 2): x =", x, "y =", y)

x, y = y, x

print("After Swapping (Method 2): x =", x, "y =", y)
