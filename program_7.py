# Attendance Summary Generator
# You are developing a simple attendance tracking system for a classroom. Each student has attendance records for 5 days, marked as:
#     'P' for Present
#     'A' for Absent
# Any other value is considered invalid and should be ignored with a warning.
# Write a Python program that processes this attendance data and generates a summary report.

students = {
    "Alice": ['P', 'A', 'P', 'P', 'A'],
    "Bob": ['P', 'P', 'X', 'A', 'P'],      # 'X' is invalid
    "Charlie": ['A', 'A', 'P', 'P', 'A']    
}

present = 0
absent = 0
max = 0
max_list = []
for ch , i in students.items():
    for j in i:
        if j == 'P':
            present = present+1
        elif j == 'A':
            absent = absent+1
        else: 
            # print("Invalid attendance status",j)    
            continue 
    # finding max present  
    if(present > max):
        max = present
        max_list = [ch]
    elif(present == max):
        max_list.append(ch)
    print(f"{ch} - Present: {present}, Absent: {absent}")
    present = 0
    absent = 0
    
print(max_list) 
