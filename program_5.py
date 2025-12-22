#task_1
emp_name = input("enter your name=")
emp_age = int(input("enter your age="))
monthly_salary = int(input("enter your salary="))
emp_name_check = True
emp_age_check = True
emp_monthly_salary_check = True

if(emp_age<18 or emp_age>60):
    print("invalid age")
    emp_age_check = False
    exit()
elif(monthly_salary<=0):
    print("invalid salary")
    emp_monthly_salary_check = False
    exit()
elif(emp_name  in 'A-Za-z'):
    print("invalid name")
    emp_name_check = False
    exit()

if(emp_name_check == True and emp_age_check == True and emp_monthly_salary_check == True):
    print("employee name=",emp_name)
    print("employee age=",emp_age)
    print("employee monthly salary=",monthly_salary)
    
#task-2:

update_name = emp_name.upper()
print("employee name in uppercase=",update_name)

#count total number of characters 
char_count = 0
for ch in update_name:
    if ch not in " ":
        char_count = char_count+1
print(char_count)

#count vowels and consonants 
vowels_count = 0
cons_count = 0
for ch in update_name:
    if ch in 'AEIOU':
        vowels_count = vowels_count+1
print("vowels are=",vowels_count)

for ch in update_name:
    if ch in 'A-Z' :
        cons_count = cons_count+1
print("consonants are=",cons_count)

#palindrome 
reversed_name = update_name[::-1]
if(update_name == reversed_name):
    print("given name is palindrome")
else:
    print("given name is not palindrome")


#task:3

yearly_salary = monthly_salary * 12

print("yearly salary = ",yearly_salary)
if(yearly_salary>1000000):
    print("you are at senior level")
    bonus = (20/100)*yearly_salary
    print("your bonus is",bonus)
      
elif(yearly_salary>= 500000 and yearly_salary<=1000000):
    print("you are at mid level")
    bonus = (10/100)*yearly_salary
    print("your bonus is",bonus)
    
else:
    print("you are at junior level")
    bonus = (5/100)*yearly_salary
    print("your bonus is",bonus)

#task4
emp_list = [101,102,103,101,104,102,105]

duplicate_id = []
for i in emp_list:
    if emp_list.count(i) > 1 and i not in duplicate_id:
        duplicate_id.append(i)
print("duplicate ids are=",duplicate_id)
unique_ids = set(emp_list)
print("total unique ids=",len(unique_ids))

#task-5

skills = input("enter your=")
skills_list = skills.split(",")
skills_set = set(skills_list)

print("total unique skills=",len(skills_set))

for i in skills_set:
    if(len(i)>5):
        print(i)

#skill aplhabetically 
for i in skills_set:
    for j in skills_set:
        if(i < j):
            print(i)
            break
        else:
            print(j)
            break 
        
#task-6
emp_depart= {"HR": 3,"IT": 8,"Sales": 5,"Finance": 2}

max_emp_dept = max(emp_depart, key=emp_depart.get)
print("department with max employees=",max_emp_dept)

min_emp_dept = min(emp_depart , key=emp_depart.get)
print("department with min employees=",min_emp_dept)

#total 
total_emp = sum(emp_depart.values())
print("total employees = ", total_emp)

    
#task-7


for i in range(1,51):
    print(i)
    if(i%4 == 0):
        continue
    if(i == 37):
        break

# TASK 8
total_paid = 0
salary_tax = monthly_salary - (0.1 * monthly_salary)
month = 0

while total_paid <= yearly_salary:
    month = month +1
    total_paid = total_paid+ salary_tax
    
    if total_paid > yearly_salary:
        break
    print(month)
    print(salary_tax)