try:
  num = int(input("Enter a number:" ))  
except ValueError:
  print("this is not a number ! plz enter the valid input ")

finally :
  print("thanku for visting the site")

# problem : Age Verification System (if-elif-else with Try-Except-Finally)
# 👨‍💼 Scenario: Ek program likho jo user se age input le aur eligibility check kare:

# 0-17: "You are a minor."
# 18-60: "You are an adult."
# 60+: "You are a senior citizen."
# Invalid Input: "Invalid input! Please enter a valid number."



try:
    age = int(input("Enter your age"))

except ValueError :
    print ("required valid input ")
    exit()

if ( age > 0 and age < 17  ):
    print("You are a minor.")

elif(age > 18 and age < 60 ):
    print("You are an adult ")

elif(age >= 60 ):
    print("You are a senior citizen.")

else:
    print("Invalid input! Please enter a valid number.")
    print("\n________________________________________\n")



# Task : Even or Odd Checker
# 👨‍💻 Scenario: Ek program likho jo user se ek number input le aur check kare ki number even hai ya odd.

try:
 num = int(input("Enter a valid number" ))
except ValueError:
 print("Invalid input! Please enter a valid number.")
 exit()

if (num % 2 == 0):
  print("The number is even ")

else :
    print("The number is odd ")

print("\n________________________________________\n")

try:
  num1 = int(input("enter a num1 "))
  num2 = int(input("enter a num2 "))
  num3 = int(input("enter a num3 "))
except ValueError:
    print("enter a valid number")
    exit()

if ( num1 > num2 and num1 > num3 ):
   print("num1 is greater among them ")

elif( num2 > num1 and num2 > num3 ):
   print("num2 is greter among them ")

elif(num3 >num1 and num3> num2 ):
   print("num3 is greater among them ")

elif( num3 == num2 and num1 == num3 and num1 == num2 ):
   print("all the numbers are equals", num1 )

elif (num1 == num2 and num1 > num3 ):
    print(num1," is greater")

elif( num2==num3 and num2 > num1):
   print(num2," is greater")

elif ( num3== num1 and num3> num2):
   print( num3," is greater")

else :  
    print(" missing condition  ")

print("\n________________________________________\n")

