# 1. Function Parameters and Return Value
# parameters
# def add_number(num1,num2):
#     result = num1 +num2 
#     return result 
# #num1 and num2 are the parametres 

# sum_result = add_number(10,5)
# print(sum_result)



#scope 
#1. local variable = jo function andar hi acccessible ho 
# 2. global varaibles  = jo function ke bhar bhi accessible ho 

def local_variable():
    local_var = "i am local" 
    print(local_var)

local_variable()
print("------------------------------")

global_var = 10

def use_global():
   
    use_global()
print("the global varaible is :",global_var)
print("------------------------------")


local_var = 10

def use_local():
    local_var = 10
    print("the local varaible is :",local_var)
use_local()

print("------------------------------")
