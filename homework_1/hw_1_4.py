#Write a Python program to find all the values in a list is greater than a specified number

list = [1, 2, 3, 4, 5, 6, 7, 100]

print(all(x > 0 for x in list))
print(all(x > 5 for x in list))
