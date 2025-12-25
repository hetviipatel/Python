# Q1 
# Remove Duplicates from a List
# logic 
# 1.create new list to store unique elements.
# 2.for loop for each element in the original list.
# 3.than check if the element is already in the new list.
# 4.if it is not present, append it to the unique list.

list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]
new_list = []
for i in list_with_duplicates:
    if i not in new_list:
        new_list.append(i)
print("list after removing duplicates:", new_list)

# Q2
# write a program to remove all occurrences of item 20.
# logic
# 1.loop for access each element in the list.
# 2.check if the element is equal to 20.
list1 = [5, 20, 15, 20, 25, 50, 20]
for i in list1:
    if i == 20:
        list1.remove(i)
print("list after removing 20:", list1)

# Q3
# Use list comprehension to create a new list containing only the numbers from a given list.
# logic
# 1.create a new list using list comprehension.
# 2.loop through each element in the original list.
# 3.check if the type of element is integer.
my_list = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'Jhon', 6]
new_list = [i for i in my_list if type(i) == int]
print("list with only numbers:", new_list)

# Q4 
# Access Nested Lists print '55'
nested_list =[[10, 20, 30], [44, 55, 66], [77, 87, 99]]
print("accessed element:", nested_list[1][1])

# Q5 Write a function to flatten a list of lists into a single, non-nested list.
# logic
# 1.create an empty list to store flattened elements.
# 2.loop through each sublist in the main list.
list_of_lists = [[1, 2], [3, 4], [5, 6, 7]]
flatten_list = []
for i in list_of_lists:
    for j in i:
        flatten_list.append(j)
print("flattened list:", flatten_list)

# Q6 Concatenate two lists index-wise
# logic
# 1.create an empty list to store concatenated elements.
# 2.loop through the range of length of one list.
# 3.append from both lists at the same index to the new list.
list_6 = ['M', 'na', 'i', 'Ke']
list_7 = ['y', 'me', 's', 'lly']
concatenated_list = []
for i in range(len(list_6)):
    concatenated_list.append(list_6[i] + list_7[i])
print("concatenated list:", concatenated_list)

# Q7
# Concatenate two lists in the following order
# logic
# 1.create an empty list to store concatenated elements.
# 2.loop for access each element in the first list.
# 3.nested loop for access each element in the second list.
# 4.append the concatenated elements to the new list.

list_8 = ['Hello ', 'take ']
list_9 = ['Dear', 'Sir']
concatenated_list_2 = []
for i in list_8:
    for j in list_9:
        concatenated_list_2.append(i + j)
print("concatenated list in specific order:", concatenated_list_2)

# Q8
# Iterate both lists simultaneously
# logic
# 1.loop for access each element in the first list.
# 2.nested loop for access each element in the second list in reverse order.
# 3.print the elements from both lists.
# 4.remove the printed element to avoid repetition
list_10 = [10, 20, 30, 40]
list_11= [100, 200, 300, 400]
for i in list_10:
    for j in list_11[::-1]:
        print(i, j)
        list_11.remove(j)
        break
    
# Q9
#Add new item to list after a specified item
# logic
# 1. find the index and insert a value.
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print("list after adding 7000:", list1)

# Q10
#Extend nested list by adding the sublist
# logic
# 1. access the nested list and extend it with the sublist.

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sublist = ["h", "i", "j"]
list1[2][1][2].extend(sublist)
print("extended nested list:", list1)

# Q11
# Replace list’s item with new value if found
# logic
# 1.loop for access each element in the list.
# 2.check if the element is equal to 20. 
# 3.if found, replace it with 200 and break the loop.
list1 = [5, 10, 15, 20, 25, 50, 20]
for i in range(len(list1)):
    if list1[i] == 20:
        list1[i] = 200
        break
print("list after replacing 20 with 200:", list1)