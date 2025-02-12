# # text = "yashika kanwer"
# # print(text[::-1])  


# # text = "Python Programming"
# # print(text[::-1])  # Output: Python

# # text = "python programmming"
# # print(text[0:6])
# # print(text[:5])
# # print(text[-6:-3])# p frist character from right and t tak vo silicing krega 

# # print(text[1:])


# #identify data types
# #1 question 
# message = 10 
# print(type(message))
# b = 3.14 
# print(type(b))
# e = [1,2,3]
# print(type(e))

# #2 question
# first_name = "john"
# last_name = "doe"
# full_name = first_name + " " + last_name
# print(full_name)



# #3 question
# message = input( "Enter your name" )
# print("welcome,")
# print(message)

# #4 Extracting a Substring (String Slicing)
# message = "hello world"
# print(message[5:]) 

# #5 reverse a string 
# message = "print "
# print(message[::-1])

# #6 question
# message = input("enter a sentence:")

# words = message.split()
# word_count = len(words)
# print("total worlds:", word_count)


# #7 question

# numbers = (1, 2, 3, 4, 2, 2, 5, 6, 2)
# count_2 = numbers.count(2)

# print("count of 2:", count_2)


# student = {
#     "name": "John Doe",
#     "age": 25,
#     "grade": "A",
#     "subjects": ["Maths", "Science", "English"]
# }
# print(student)
# student["age"] = 50

# print(student)

student = {"name": "Amit", "age": 20}

print(student)

student = {"name": "Amit", "age": 20}
for key, value in student.items():
    print(f"{key}: {value}")

