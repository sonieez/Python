def dep_salary(connect):
    cursor = connect.cursor()
    departments = {}
    cursor.execute("select * from employees_department")
    for row in cursor:
        dep_id = row[2]
        salary = row[1]
        if dep_id not in departments:
            departments[dep_id] = []
        departments[dep_id].append(salary)

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
    for key, value in salary.items():
        print(f"{key}: Max salary = {value[0]}, Min salary = {value[1]}")

