

# used to input numbers 


input== any ("0/1/2/3/4/5/6/7/8/9")
any == [ 'a (int)' ]
any == [ 'b (int)' ]

#use the function to add numbers together

def add(a, b):
    return a + b

total = add(2, 2)
print(total)

#use the function to subtract numbers

def subtract(a, b):
    return a - b

total = subtract(2, 2)
print(total)

#use the function to multiply numbers

def multiply(a, b):
    return a * b

total = multiply(2, 2)
print(total)

#use the function to divide numbers

def divide(a, b):
    return a / b

total = divide(2, 2)
print(total)

#select operation

input = ("select function")
print("add")
print("subtract")
print("multiply")
print("divide")

# take input

print = input("enter pick (1/2/3/4/5/6/7/8/9/0): ")

# check if user wants to do another calculation
next_calculation = input ( "how about another one?: ")


