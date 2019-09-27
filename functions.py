########################
"""
def hello():
    """this functions prints hello world"""
    print("hello world")

# calling the function
hello()

# what you can do with docstring?
print(hello.__doc__)

"""

########################
"""

def my_func(param1 = "defult"):
    print("This is {}".format(param1))

my_func()
"""

########################
# printing something vs return function
"""

def hello():
    print("hello")

hello()
########################


def hello():
    print("hello")

hello() #no output
result = hello()
print(result)
"""

def addNum(num1, num2):
    return num1+num2

result = addNum(2,3)
print(result) #5

result2 = addNum("2", "3") 
print(result2) #23
# the above will concatenate strings together which we don't want to do, 
# ERROR
# so it's better that we check the type of the num first, then only add

# checking type before adding

def addNum(num1, num2):
    if type(num1) == type(num2) == type(10):
        return num1+num2
    else:
        return "sorry, I need Integers"

result1 = addNum(2,3)
print(result) #5

result2 = addNum("2", "3") 
print(result2) #sorry, I need Integers


