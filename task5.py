#Lists, Tuples, Dictionaries, and Sets

my_list = ["variables", "data types", " data structure", "function"]
my_list.append('oops')
print(my_list)

print("\n----------------------------------------\n")


#tuples
numbers = [10, 25, 5, 89, 14, 45]
max_num = max(numbers)
min_num = min(numbers)
print("maximun number :", max_num)

print("minimum number :", min_num)
print("\n----------------------------------------\n")


# Dictionaries
student = {"name": "Rahul", "age": 20, "marks": 90}

for key, value in student.item():
    print(f"{key} : {value}")
    print("\n----------------------------------------\n")


#set operation 
football_players = {"Rahul", "Shyam", "Amit", "soham", "neha"}
cricket_players = { "Amit", "Rohan", "neha", "soham", "yash"}
common_players =  football_players.intersection(cricket_players)
print("\n----------------------------------------\n")


print("common players between football and cricket :", common_players)
all_players = football_players.union(cricket_players)
print("all unique players in both teams:",all_players)
print("\n----------------------------------------\n")
