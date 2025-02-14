# while loop tb tk chlta h jb tk condition true hoti h . jese hi ondiytion false hoti h loop terminate hota h ..overall hm kh skte h  ki whlie loop condtiion based hota h 
# main concept 
# counter variable jo ilteration ko count krta h 
# flag variables logical condition ko track krne me kaam aata h jese boolean vaiables 
# active loop yhe bhi flag varible ki thre hote h jo btate h ki loop chlega ya nhi chlega 

#count variables 
# 🔹 Example:
# 👉 Hum count kar rahe hain ki shop me kitne customers aaye.

count = 0  # abhi koi customer nahi aaya  
while count < 5: 
     print(f"Customer {count + 1} entered the shop.")  
     count += 1  

#  Loop Active
#  Yeh ek flag variable ki tarah hota hai, jo yeh decide karta hai ki loop chalega ya nahi.
loop_active = True 
count = 0 
while loop_active:
    print(f"customer {count+1} enetered the shop")
    count += 1 

    if count >= 5:
        loop_active = False 

# While Loop Tasks
# 🔹 Task 1: Counting from 1 to 10
count = 1 
while count <= 10:
    print(count)
    count += 1 

#  🔹 Task 2: Print "Hello World" 5 Times  
count = 1 
while count <= 10 :
    print ("hello world ")
    count += 1

#  🔹 Task 3: Print Odd Numbers from 1 to 10
count = 1 
while count <= 10 : 
    print("odd numbers:", count )
    count += 2
  
# Task 4 : Print even number from 1 to 10 
count = 2
while count <=10:
    print("even number:", count)
    count += 2

    #  Task 5: Sum of First 5 Natural Numbers
num = 1 
sum = 0 

while num <= 5:
    sum += num 
    num += 1

print("Sum:",sum)

  


