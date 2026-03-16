def dep_salary(connect):
    cursor = connect.cursor()
    departments = {}
    cursor.execute("select * from employees_department")
    for row in cursor:
        dep_name = row[2].lower().strip()
        salary = row[1]
        if dep_name not in departments:
            departments[dep_name] = []
        departments[dep_name].append(salary)

    salary = {}
    for key, value in departments.items():
        dep = key
        max_salary = max(value)
        min_salary = min(value)
        if dep not in salary:
            salary[dep] = []
        salary[dep].append(max_salary)
        salary[dep].append(min_salary)

    return salary

def output(salary):
    print("\n--Departments Statistics--")
    print("\nDepartment | Max salary | Min salary")
    for key, value in salary.items():
        print(f"{key.upper():<10} | {value[0]:<10} | {value[1]}")

