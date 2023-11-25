employee_file=open("employees.txt","r")
for emp in employee_file.readlines():
    print(emp)
employee_file.close()