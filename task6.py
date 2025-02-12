# Task 6: Operators: Arithmetic, Assignment, Comparison, Logical 

# Arithmetic

first_number = int(input("Enter the first number "))

second_number =int( input("Enter the second number "))

# Addition

sum_result = (first_number + second_number)
print(sum_result)

# Subtraction

diff_result = (first_number - second_number)
print(diff_result)

# Multiplication

prod_result = (first_number * second_number)
print(prod_result)

# Division

div_result = (first_number / second_number)
print(div_result)

# Modulus

mod_result = (first_number % second_number)
print(mod_result)

# Floor Division

floor_div_result = (first_number // second_number)
print(floor_div_result)

# Exponentiation

exp_result = (first_number ** second_number)
print(exp_result)
print("\n_________________________________________________/n")

# 2. Assignment Operators = vaiables me value assing krne ke liye 
 
num = int(input("Enter the number :"))
print("your number is :",num)
num += int(input(f"Give a number which you want: {num} + ", ))
print("after operation your output is:",num)

num -= int(input(f"Give a number which you want: {num} - ", ))
print("after operation your output is:",num)

num *= int(input(f"Give a number which you want: {num} * ", ))
print("after operation your output is:",num)

num /= int(input(f"Give a number which you want: {num} / ", ))
print("after operation your output is:",num)

num //= int(input(f"Give a number which you want: {num} // ", ))
print("after operation your output is:",num)

print("\n_________________________________________________/n")

# 3. Comparison Operators
# == (equal), != (not equal), > (greater than), < (less than), >= (greater than or equal to), <= (less than or equal to)

num1 = int(input("enter a  first number :"))
num2 = int(input("enter a second number :"  ))
print(f"num1 is equal to num2:,{num1 == num2}")

print(f"num1 is not equal to num2:,{num1!= num2}")

print(f"num1 is greater than num2:,{num1 > num2}")
print(f"num1 is lesser than num2:, {num1 <num2}")
print(f"num1 is equal to or greater than num2 :, {num1 >= num2}")

print(f"num1 is equal to or lesser than num2:, {num1 <= num2}")

print("\n_________________________________________________/n")

# 4. Logical Operators

# and (both conditions are true), or (at least one condition is true), not (negation)

age = 20 
if age <= 18 and age >= 65 :
    print("Person is eligible for voting")
else :
    print("Person is not eligible for voting")

# Logical OR operation


password_match = False 
fingerprint_match = True

if password_match or fingerprint_match :
    print("unlocked")

else:
    print("locked")
    print("Please provide the vaild password and fingerprint ")

    #  'not' operator

is_ranning = False
if not is_ranning:
    print("can go outside!")
else:
        print("not able to go outside! ")




