def data_insert(name, salary, department, connect):
    cursor = connect.cursor()
    cursor.execute(
        "INSERT INTO employees_department(e_name, e_salary, d_id) VALUES (:1, :2, :3)", (name, salary, department)
    )
    connect.commit()


def data_select(connect):
    cursor = connect.cursor()
    cursor.execute(
        "select * from employees_department"
    )
    return cursor.fetchall()

def salary_check(connect):
    cursor = connect.cursor()
    cursor.execute("select * from employees_department")
    high_salaries = []
    for row in cursor:
        if row[1] > 500:
            high_salaries.append(row)

    n = len(high_salaries)
    for i in range(n):
        for j in range(0, n - i - 1):
            if high_salaries[j][1] < high_salaries[j + 1][1]:
                high_salaries[j], high_salaries[j+1] = high_salaries[j+1], high_salaries[j]

    return high_salaries

