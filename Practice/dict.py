#Q1
# Perform basic dictionary operations 
# Add New Key-Value Pair
# Modify Value Access Key
# remove Key-Value Pair
# get item
# check id key exists
# clear

dict_1 = {'name': 'Alice', 'age': 35, 'city': 'New York'}
# add new key-value pair
dict_1['profession'] = 'Doctor'
# modify value
dict_1['age'] = 40
print("Access city's value",dict_1['city'])
print(dict_1)
del dict_1['profession']
for i in dict_1.items():
    print(i)
# check if key exists
if 'age' in dict_1:
    print("True")
# clear dictionary
dict_1.clear()
print(dict_1)

# Q2
# Dictionary from Lists
# logic
# 1.loop for the range of length of keys list.
# 2.assign each key from keys list to it's value from values list.
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict_2 = {}
for i in range(len(keys)):
    dict_2[keys[i]] = values[i]
print("dictionary from lists:", dict_2)

# Q3
# Merge Two Dictionaries
dict_3 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict_4= {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# update method to merge two dictionaries
dict_3.update(dict_4)
print("merged dictionary:", dict_3)

# Q4
# Count Character Frequencies
# logic
# 1.create an empty dict
# 2.loop for each character in the string.
# 3.check if the character is already a key in the dict.

string = "jessa"
freq_ch = {}
for char in string:
    if char in freq_ch:
        freq_ch[char] = freq_ch[char] + 1
    else:
        freq_ch[char] = 1
print("character frequencies:", freq_ch)

# Q5
# Access Nested Dictionary
data = {'person': {'name': 'Alice', 'age': 30}}
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print("accessed nested value:", data["person"]["age"])
print("accessed nested value:", sampleDict["class"]["student"]["marks"]["history"])
sampleDict["class"]["student"]["name"] = "jessa"
print("after modified",sampleDict)

# Q6
# Initialize dictionary with default values
# logic
# 1.create an empty dict.
# 2.loop through each element in the employees list.
# 3.assign each employee name as key and default values as value.
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
new_dict = {}
for i in employees:
    new_dict[i] = defaults
print("initialized dictionary:", new_dict)

# Q7
# Delete a list of keys from a dictionary
# logic
# 1.loop through each key in the keys list.
# 2.delete the key from the dictionary.
dict_5 = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
keys = ["name", "salary"] 
for key in keys:
    del dict_5[key]
print("after deleting name key:", dict_5)

# Q8
# Check if a value exists in a dictionary
dict_6 = {'a': 100, 'b': 200, 'c': 300}
if 200 in dict_6.values():
    print("value exists")

# Q9
# Rename a key in a dictionary
dict_7 =  {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
dict_7['location'] = dict_7.pop('city')
print("after renaming key:", dict_7)

# Q10
# Get the key of a minimum value from the dictionary
# logic
# 1.initialize min_key with the value of first key.
# 2.loop through each key in the dictionary and check condition.
dict_8 ={
  'Physics': 82,
  'Math': 65,
  'history': 75
}
min_key = dict_8["Physics"]
for value in dict_8:
    if dict_8[value] < min_key:
        min_key = dict_8[value]
print("minimum value key:", min_key)

# Q11
# Change value of a key in a nested dictionary
dict_9 = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
dict_9["emp3"]["salary"] = 8500
print("after changing nested value:", dict_9)

# Q12
# invert a dictionary
# logic
# 1.create an empty dict.
# 2.assign value as key and key as value in the new dict.
dict_10 = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = {}
for key, value in dict_10.items():
    inverted_dict[value] = key
print("inverted dictionary:", inverted_dict)

# Q13
# sort dictionary by key
# sort dictionary by value
# logic
# 1.use sorted() with items() to sort by key.
# 2.use sorted() with items() and lambda function to sort by value.

dict_11 =  {'apple': 3, 'zebra': 1, 'banana': 2, 'cat': 4}
print(sorted(dict_11.items()))
print(sorted(dict_11.items(), key=lambda x: x[1]))

# Q14
#  Check if All Values are Unique
# logic
# 1.get all values from the dictionary.
# 2.convert the values list to a set and compare its length with the original list.
# 3.if lengths are equal, all values are unique.
dict_12 = {'a': 1, 'b': 2, 'c': 3,}
dict_13 = {'x': 10, 'y': 20, 'z': 10} 

def are_values_unique(d):
    values = list(d.values())
    return len(values) == len(set(values))
print(are_values_unique(dict_12))  # True
print(are_values_unique(dict_13))  # False