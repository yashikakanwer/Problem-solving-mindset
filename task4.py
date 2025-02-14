#Exploration of Strings
#college education problems
college_problem = input("what is the biggest problem you face in college education or during college time.")
print("\nThanku you for sharing your concern.")
print("Problem statment:")
print( college_problem)


# String manipulation
# Taking user input for  college education problem 
colleges_problem = input("Enter a college education problem :")

# now applying different string methods
print("\nApplying string methods:")

# Convert all characters to uppercase
print("1.uppercase:", colleges_problem.upper()) 

# Convert all characters to lowercase
print("2.lower:", colleges_problem.lower())

# splitting the string:
print("3.split():", colleges_problem.split())

#  String Concatenation
concatenated_string = "You mentioned: " + colleges_problem + ". We will work on solving it!"
print("\nConcatenated String:")
print(concatenated_string)

# Finding the word  
colleges_problem = "lack of knowledge "
word_find = "of"
position = colleges_problem.find(word_find)
if position != -1:
    print(f"position of '{word_find} in the string",position)
else:
    print(f"'{word_find}'not found in the input.")

    #  Replacing words 
colleges_problem = "Lack of practical learning in college education."
replaced_problem = colleges_problem.replace("college", "university")

print(replaced_problem)

#  String Formatting 
colleges_problem = "Lack of practical learning in college education."
formatted_output = f"Your problem '{colleges_problem}' is a major issues in system."
print(formatted_output)

text = "python programmming"
print(text[0:6])
print(text[:5])
print(text[-6:-3])# p frist character from right and t tak vo silicing krega 

print(text[1:])# reversing the string 