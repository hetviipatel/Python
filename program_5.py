#task_1
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
   
#task-2:

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


#task:3

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
print("Bonus Amount is =", format(bonus, ","))
    

#task4
emp_list = [101,102,103,101,104,102,105]
duplicate_count = 0

duplicate_id = []
for i in emp_list:
    if emp_list.count(i) > 1 and i not in duplicate_id:
        duplicate_id.append(i)
        duplicate_count = duplicate_count + 1
    print("total duplicate ids=",duplicate_count)
print("duplicate ids are=",duplicate_id)
unique_ids = set(emp_list)
print("total unique ids=",len(unique_ids))

#task-5

skills = input("Enter skills=")

# Convert to list 
skills_list = skills.split(",")
#remove space
for skill in skills_list:
    skill = skill.strip()
    skills_list.append(skill)


skills_set = set(skills_list)

print("total unique skills:", len(skills_set))


print("skills with more than 5 characters:")
for skill in skills_set:
    if len(skill) > 5:
        print(skill)

# Convert set back to list for sorting
skills_list = list(skills_set)

# Manual alphabetical sorting (Bubble Sort)
n = len(skills_list)
for i in range(n):
    for j in range(0, n - i - 1):
        if skills_list[j] > skills_list[j + 1]:
            skills_list[j], skills_list[j + 1] = skills_list[j + 1], skills_list[j]

# Print sorted skills
print("skills sorted alphabetically:")
for skill in skills_list:
    print(skill)

        
#task-6
emp_depart= {"HR": 3,"IT": 8,"Sales": 5,"Finance": 2}

max_emp_dept = max(emp_depart, key=emp_depart.get)
print("department with max employees=",max_emp_dept)

min_emp_dept = min(emp_depart , key=emp_depart.get)
print("department with min employees=",min_emp_dept)

#total 
total_emp = sum(emp_depart.values())
print("total employees = ", total_emp)

    
# #task-7


for i in range(1,51):

    if ( i == 37):
        break
    if(i % 4 == 0):
        continue
    print(i)
    
#  TASK 8

total_paid = 0
salary_tax = monthly_salary * 0.9  
month = 0

while total_paid < yearly_salary:
    month += 1
    total_paid += salary_tax

    print(f"Month {month}: Salary Paid = {salary_tax}, Total Paid = {total_paid}")
