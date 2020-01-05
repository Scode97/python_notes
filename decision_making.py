##################################
### if,elif, else Statements #####
##################################

# *Indentation is extremely important in Python*

# a program to check if a number is +ve and print an appropriate message
"""
num = 1
num = -1
if num>0:
    print("{} is a +ve number".format(num))

print("This is printed anyways")
"""

##################################

# a program to check if a number is +ve or -ve and print an appropriate message

"""
num = 1
num = -1
num = 0
if num>=0:
    print("+ve or zero")
else:
    print("-ve number)

print("This is printed anyways")
"""

##################################

# a program to check if a number is +ve or -ve or zero and print an appropriate message

"""
num = 1
num = -1
num = 0
if num>0:
    print("+ve or zero")
elif num==0:
    print("zero")
else:
    print("-ve number)

print("This is printed anyways")
"""

##################################

# prompt the user to enter a number and check if the number is +ve or -ve
# or zero and display an appropriate message

"""
num = float(input("Enter a number:"))
if num>=0:
    if num==0:
        print("zero")
    else:
        print("+ve number")
else:
    print("-ve number)

print("This is printed anyways")
"""
