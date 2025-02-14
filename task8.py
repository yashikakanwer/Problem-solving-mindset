list = ["apple", "mango", "papaya" ]
for list in list :
     print("-" + list)


# List Ke Elements Ke Saath Index Print Karna
colors = ["Red", "Green", "Blue", "Yellow"]
for index, color in enumerate(colors, start=1):
    print(f"{index}. {color}")

# # Task 1: Loop with List(multiple by 2 each element )
numbers = [2,4,6,8,10] 
for num in numbers :
    print(num*2)


# # Task 2: Loop with String
# # 👉 Ek string "Python" di gayi hai. Har character ko uppercase me print karo.

text = "phyton"
for char in text :
   print(char.upper())

#     # Task 3: Loop with Dictionary
# # 👉 Ek dictionary di gayi hai:

student = {"name": "Amit", "age": 21, "course": "CSE"}
for key,value  in student .items():
     print(key, ":", value)

#  Mini Project: Topic Iteration System
# 👉 Ek interactive program banayein jo learning topics ko iterate karega aur user se next topic dekhne ke liye input lega.


learning_topics = [ "oops", "variables " , "web development ", "algorithms", "Ai" ] 
for topic in learning_topics:
    print("current topic :",topic)
    user_input = input("want to read futher? (yes or no ?)").strip()
    if user_input == "no" :
        print("learning session ended")
        break 


#  Task:
# Aap ek quiz system banao jisme ek ek karke questions display honge. Har question ke baad user se poocha jayega ki agla question dekhna hai ya nahi.

questions = [
"What is the full form of OOP?\n a) Object-Oriented Programming\n b) Oriented Object Programming\n c) Online Object Processing\n d) None of the above",
    "What is the time complexity of binary search?\n a) O(n)\n b) O(n log n)\n c) O(log n)\n d) O(1)",
    "Which data structure works on LIFO?\n a) Queue\n b) Stack\n c) Linked List\n d) Tree"
]
for question in questions :
    print ("\nquestion : ",question)

    user_input = input( "\nwant to display the next question? (yes/no)" ).strip().lower()
    if user_input == "no":
        print("thanku for visitng session ended ")

    
        break

# 📝 Task:
# Aap ek To-Do List Manager banao jisme user apne tasks dekh sake aur next task pe move kar sake
tasks = [ "complete the python assigment" , "revise the dsa ", "work on the web developemt " , "find the re[ort on Ai",]

for task in tasks :
    print ("task:", task)
   

    user_input = input("is the  first task complete ? want next task or not ? yes or no ?")
    if user_input == "no":
        print("ok well and goood ")
        break