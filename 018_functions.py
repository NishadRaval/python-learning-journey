# 1. Simple function
def greet():
    print("Hello Nishad!")

greet()

# 2. Function with parameters
def greet_user(name):
    print("Hello", name)

greet_user("Nishad")
greet_user("Rahi")

# 3. Function with return value
def add(a, b):
    return a + b

result = add(10, 20)
print("Sum =", result)

# 4. Function with default argument
def welcome(name="Guest"):
    print("Welcome", name)

welcome()
welcome("Nishad")

# 5. Function to check even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(10))
print(check_even_odd(7))

# 6. Function to find greater number
def greater(a, b):
    if a > b:
        return a
    else:
        return b

print("Greater number:", greater(25, 30))

# 7. Function to calculate square
def square(num):
    return num * num

print("Square:", square(5))