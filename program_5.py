# You are required to build a simple Employee Management System for a small company.
# Complete all the subtasks mentioned below as part of this problem statement.

# TASK 1: INPUT & VALIDATION
# Take the following inputs from the user:
# Employee Name
# Employee Age (input as string)
# Monthly Salary

emp_name = input("enter your name=")
emp_age = input("enter your age=")
monthly_salary = input("enter your salary=")

if not emp_name.isalpha():
    print("invalid name")
    exit()
    
if not emp_age.isdigit():
    print("invalid age")
    exit()

emp_age = int(emp_age)
if(emp_age < 18 or emp_age > 65):
    print("invalid age for employee")
    exit()

if not monthly_salary.isdigit():
    print("invalid age")
    exit()
    
monthly_salary = float(monthly_salary)
if(monthly_salary <= 0):
    print("invalid salary")
    exit()

print("employee name=",emp_name)
print("employee age=",emp_age)
print("employee monthly salary=",monthly_salary)
   
#TASK 2: NAME ANALYSIS (STRING LOGIC)
# Print the name in uppercase
# Count total number of characters (excluding spaces)
# Count vowels and consonants separately
# Check whether the name is a palindrome

update_name = emp_name.upper()
print("employee name in uppercase=",update_name)
update_name = update_name.replace(" ","")

#count total number of characters 
print("total number of characters =",len(update_name))

#count vowels and consonants 
vowels_count = 0
cons_count = 0
for ch in update_name:
    if ch in 'AEIOU':
        vowels_count = vowels_count+1
    elif ch.isalpha():
        cons_count = cons_count+1
print("vowels count=",vowels_count)
print("consonants count=",cons_count)

#palindrome 
reversed_name = update_name[::-1]
if(update_name == reversed_name):
    print("given name is palindrome")
else:
    print("given name is not palindrome")


#task 3: SALARY DECISION LOGIC

# Calculate:
# Yearly salary
# Employee level based on yearly salary:
#     > 1,000,000  → Senior Level
#     500,000–1,000,000 → Mid Level
#     < 500,000 → Junior Level

# Bonus Calculation:
# Senior → 20% of yearly salary
# Mid → 10% of yearly salary
# Junior → 5% of yearly salary

yearly_salary = monthly_salary * 12

print("Yearly Salary:", yearly_salary)

if yearly_salary > 1_000_000:
    level = "Senior Level"
    bonus_rate = 0.20

elif yearly_salary >= 500_000:
    level = "Mid Level"
    bonus_rate = 0.10

else:
    level = "Junior Level"
    bonus_rate = 0.05

bonus = round(yearly_salary * bonus_rate, 2)

print("Employee Level is=", level)
print("Bonus Amount is =", format(bonus, ",")) #formatted with commas
    

#TASK 4: EMPLOYEE ID DUPLICATE CHECK (LIST + LOGIC)
# Given a list of employee IDs:
# [101, 102, 103, 101, 104, 102, 105]
# Detect and print duplicate IDs
# Print total unique employee IDs
# Print total duplicate count

emp_list = [101,102,103,101,104,102,105]
duplicate_count = 0
duplicate_id = []

#detecting duplicate ids
for i in emp_list:
    if emp_list.count(i) > 1 and i not in duplicate_id:
        duplicate_id.append(i)
        duplicate_count = duplicate_count + 1
    print("total duplicate ids=",duplicate_count)
print("duplicate ids are=",duplicate_id)
unique_ids = set(emp_list)
print("total unique ids=",len(unique_ids))

# TASK5:SKILL ANALYSIS (SET + LOOP LOGIC)

# Take employee skills as a comma-separated string input.
# Convert skills into a set
# Print total unique skills
# Print skills having more than 5 characters
# Sort skills alphabetically WITHOUT using sorted()

skills = input("Enter skills=")

# Convert to list 
skills_list = skills.split(",")
print(skills_list)
#remove space
skill = skills.strip()
skills_list.append(skill)

# Convert to set to get unique skills
skills_set = set(skills_list)

print("total unique skills:", len(skills_set))

#more than 5 characters
print("skills with more than 5 characters:")
for skill in skills_set:
    if len(skill) > 5:
        print(skill)
skills_list = list(skills_set)

# alphabetical sorting
n = len(skills_list)
for i in range(n):
    for j in range(0, n - i - 1):
        if skills_list[j] > skills_list[j + 1]:
            skills_list[j], skills_list[j + 1] = skills_list[j + 1], skills_list[j]

# Print sorted skills
print("skills sorted alphabetically:")
for skill in skills_list:
    print(skill)

        
#task-6:DEPARTMENT ANALYSIS
# Find department with maximum employees
# Find department with minimum employees
# Calculate total employees in the company

emp_depart= {"HR": 3,"IT": 8,"Sales": 5,"Finance": 2}

#max employees
max_emp_dept = max(emp_depart, key=emp_depart.get)
print("department with max employees=",max_emp_dept)

#min employees
min_emp_dept = min(emp_depart , key=emp_depart.get)
print("department with min employees=",min_emp_dept)

#total 
total_emp = sum(emp_depart.values())
print("total employees = ", total_emp)

    
# task-7 LOOP CONTROL LOGIC

# Print numbers from 1 to 50
# Skip numbers divisible by 4
# Stop the loop completely when the number reaches 37


for i in range(1,51):
    if ( i == 37):
        break
    if(i % 4 == 0):
        continue
    print(i)
    
# TASK 8
# Deduct 10% tax from monthly salary
# Add net salary to total paid amount
# Stop simulation if total paid exceeds yearly salary
# Print month number and net salary paid each month

total_paid = 0
salary_tax = monthly_salary * 0.9  
month = 0

while total_paid < yearly_salary:
    month = month+ 1
    total_paid  = total_paid+ salary_tax

    print(f"Month {month}: Salary Paid = {salary_tax}, Total Paid = {total_paid}")
