# Python program to find sum of elements in list
tatal = 0

# creatimg a list
list1 = [11, 5, 17, 18, 23]

# Iterate ech element in list
# and add them in varial total
for ele in range(0, len(list1)):
    total = total + list1[ele]
# printing total value
print("Sum of all elements in given list: ", total)