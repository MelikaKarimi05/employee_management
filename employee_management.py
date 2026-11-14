#employees_names
employees_names=["melika","melina","mohammad","zahra","melina","farhad","mahsa"]
print(f"your employees are{employees_names}")
#new employees
new_employee_names=input("do you want to add a new employee?(yes,no)").lower()
while new_employee_names=="yes":
   new_employee_name=input("please enter a new employee name:").lower()
   question=input('done?(yes/no)')
   if question=="yes":
    employees_names.append(new_employee_name)
    print(employees_names)
    break
   else:
    employees_names.append(new_employee_name)
    continue
#we want cheack how many emlpoyees are repeated!
found_employee=input("enter the employee name you want to search:").lower()
number_of_employees=employees_names.count(found_employee)
print(f"you have {number_of_employees} {found_employee} in employees names")
#if there are two or more , we will remove one!
if number_of_employees>2:
  question=input("do you want to remove one of them?(yes/no)").lower()
  if question=="yes":
   employees_names.remove(found_employee)
   print(employees_names)
   print("one employee was removed successfully")
  else:
    print("no employee was removed")
 