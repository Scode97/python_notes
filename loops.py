## For Loop with a list
"""
# Perform an action with each element
seq = [1,2,3,4,5]

for item in seq:
    print(item)


# Perform an action for every element but doesn't actually involve the elements
for item in seq:
    print('hello')
"""

"""
# program to find the sum of all the numbers stored in a list

list = [6,4,5,3]
sum = 0
# iterate over the list

for val in list:
    sum = sum + val
print("The sum is ", sum)

"""

"""
## For Loop with a Dictionary
dic = {"sara":3,"maryam":4,"samira":29}
# 1
for key in dic:
    print("This is the key")
    print(key)
    print("This is the value")
    print(dic[key])
    print("\n")

# 2
for item in dic:
    print(item)

# 3
for item in dic.keys():
    print(item)

# 4
for item in dic.values():
    print(item)

"""

"""
### WHILE LOOPS 

# While loops allow us to keep on performing an action until a condition
# becomes true. 


i = 1
while i < 5:
    print('i is: {}'.format(i))
    i = i+1

    