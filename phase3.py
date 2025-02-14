"""Question 1: Positive, Negative, or Zero? (If-Else)"""
num = int(input("enter a valid number :"))
if num < 0 :
    print("the number is negative")

elif num > 0 :
        print("the number is positive")


else :
      print ("zero")

# 🔹 Question 3: Print 1 to 10 (For Loop)

for i  in range(1, 11):
      print("the number is :",i)

#  Question 6: Skip 5 Using Continue (For Loop)

for i in range(1, 11):
    if i == 5:
        continue 
    print(i)

# # Multiplication Table (If-Else + For Loop + While Loop)
# # 👉 Task:

# # User se ek number input lo.
# # For loop ka use karke uska multiplication table (1 to 10) print karo.
# # If-Else ka use karke check karo ki number positive hai ya nahi.
# # While loop ka use karke baar-baar table generate karne ka option do.


while True :
    num = int(input("\nEnter a positive number for its multiplication table:"))

    if num <= 0:
        print("plz print a valid  num ")
    else :
        print("\nMultiplacation of a table{num}")
        for i in range(1,11):
            print(f"{num}*{i}={num*i}")

    again = input("\nDo you want to try another number? (yes/no): ")
    if again != "yes":
        print("Thanks for using the table generator! ")
        break


# """Task Instructions:
# User se PIN input lo (Correct PIN = 1234)
# Agar PIN sahi hai toh options dikhao:
# 1: Check Balance
# 2: Withdraw Money
# 3: Exit
# Balance check karne pe available balance dikhao.
# Withdraw karne pe check karo ki balance sufficient hai ya nahi.
# Wrong PIN par maximum 3 attempts ke baad exit ho jaye.
# Loop tab tak chale jab tak user 'Exit' nahi karta."""




correct_pin = 1234
balance = 5000
attempt = 3  
active = True 


while attempt > 0:
    Pin = input("Enter your PIN: ")

    if int(Pin) == correct_pin:  
        print("\n PIN Verified Successfully!\n")
        
        
        while active:
            print("\n ATM Menu:")
            print("1 Check Balance")
            print("2 Withdraw Money")
            print("3 Exit")

            choose = input("\nSelect an option (1/2/3): ")

            if choose == "1":
                print(f"\n Your Current Balance: ₹{balance}")

            elif choose == "2":
                amount = int(input("\nEnter amount to withdraw: ₹"))  

                if amount > balance:
                    print(" Insufficient Balance! Try again.")
                else:
                    balance -= amount  
                    print(f" Withdrawal Successful! New Balance: ₹{balance}")

            elif choose == "3":
                print("\n Exiting... Thank you for using our ATM!")
                active = False  

            else:
                print(" Invalid Option! Please select again.")

        break  

    else:
        attempt -= 1  
        print(f" Incorrect PIN! Attempts left: {attempt}")

        if attempt == 0:
            print("\n Maximum attempts reached! Exiting ATM.")



# task next 

#  Task: Number Storing List with Names
# Ek empty list banayenge jisme naam aur number store honge.
# While loop use karenge jo tab tak chalega jab tak user stop na kare.
# Har entry me name aur number input lenge.
# Jab user no likh dega, tab loop band ho jayega.

contacts = {}
while True :
 name = input("Enter your name")
 number = int(input("Enter your phone number"))

 contacts[name] = number

 choice = input("do you want more to store the contact.( yes/no)").strip().lower()
 if choice == "no":
  print("/n thnku for visting ")
  break
 
 print("\nstored contact :")
 for name, number in contacts.item():
  print(f"Name:{name}, Number:{number}")
  



