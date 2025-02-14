# function ek aisa block of code hote h jo specific task perform karte h 
 
# Example 1: Ek Simple Function Jo Greeting Print Kare
"""def greet():
    print("welcome to phyton world")

greet()
"""
# Example 2: Function Jo User Ka Naam Accept Kare

"""def personalized_greet(name):
    print(f"Hello, {name}! Welcome to Python!")
personalized_greet("rahul")
personalized_greet("ram")"""


"""# Q3: Function with Parameters (Add Two Numbers)
def sum_num(a,b):
    return a + b
result = sum_num(5, 3)
print("sum:",result)"""

# Q3: Function with Default Parameter (Greet a Person)
"""def greet(name = "guest"):
    print(f"hello,{name}!")

greet("aman")
greet()"""

# Q4: Function to Check Even or Odd

"""def check_even_odd(n):
    if n % 2 == 0:
        print(f"{n} is even ")
    else:
        print(f"{n} is odd ")

check_even_odd(10)
check_even_odd(7)"""


# Q4: Ek function likho jo kisi number ka square return kare.

"""def square(num):
   return num ** 2

print(square(10))
print(square(4))"""

# Q5: Ek function likho jo ek string ko reverse kare.
"""def reverse_string(s):
    return s[:: -1]
print(reverse_string("python"))"""

# Simple Calculator using Functions

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

def calculator():
    while True:
        print("\nSimple Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = int(input("Select one of the options (1-5): "))

        if choice == 5:
            print("Exiting the calculator. Goodbye!")
            break  

        if choice in [1, 2, 3, 4]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                print(f"Result: {add(num1, num2)}")
            elif choice == 2:
                print(f"Result: {sub(num1, num2)}")
            elif choice == 3:
                print(f"Result: {multi(num1, num2)}")
            elif choice == 4:
                print(f"Result: {divide(num1, num2)}")
        else:
            print("Invalid choice! Please choose a number between 1-5.")

calculator()




