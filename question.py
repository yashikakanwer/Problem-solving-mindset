# Q3. list A: 5 elements integer , list B:5 string, We have to merge both of the list and make another list c which contains all the elements of both list in the sequence of integer goes to even and strings goes to odd places.
# what we have to do:
# - We have to make a multi dimensional list which have only five elements (each string contain one integer or each even element contain odd element).
# - The multi dimensional list should be in logical format and able to parse every element by the python and make the list c and it divided into list a and list b original form.

# we have to make a two list 
# list A : 5 integer 
#list B: 5 string 
#list c : merged of a and b in which integer at even place and string at odd place 
# now created multidimension list = key value pair ....key = B((odd)  and  pair = A(even)
# now extract key value pairs and back to c again 
# extract a and b from c ..... integer(even) A and string(odd)B

#step1
listA = [1, 2, 3, 4, 5]   
listB = ["A", "B", "C", "D", "E"]

print("List A:", listA)
print("List B:", listB)

#step 2     MERGING
listC = []
for a, b in zip(listA, listB):
    listC.append(a)  # Integer at even 
    listC.append(b)  # String at odd 

print("Merged List C:", listC)  

#step 3    Ab multidimesion list listD
#  keys (strings) aur values (integers) 


listD = [{B: A} for B, A in zip(listB, listA)]
print("Multi-Dimensional List:", listD)

# Step 4: Extract Lists A and B from List D
extracted_keys = []  # Stores strings by append
extracted_values = []  # Stores integers

for d in listD:
    for k, v in d.items():  # key-value pairs
        extracted_keys.append(k)
        extracted_values.append(v)

print("Extracted List B (Strings):", extracted_keys)  
print("Extracted List A (Integers):", extracted_values)  






