#project:
# 1) db.py
# 2) validation.py(datalarin valid olub olmamagi - menfi maas, dep id duzdu ya yox)
# 3) employee.py - insert, select, maasi 5000den cox olan (azalma sirari ile)
# 4) statistics.py - depertamentde maksimum, minimum salary, qrafik
# 5) appdb.py
#ad, maas, dep_id

from db import get_connection, create_table
from validation import is_valid
from employee import data_insert, data_select, salary_check
from statistics import dep_salary, output


def main():
    while True:
        connection = get_connection()
        print('\nOptions:')
        print('1. Insert employee')
        print('2. View departments and employees')
        print('3. Department statistics')
        print('4. Descending salaries')
        print('0. Exit')

        choice = int(input('\nEnter your choice: '))

        if choice == 1:
            name = input("Enter employee name: ")
            salary = int(input("Enter employee salary: "))
            department_id = int(input("Enter department id: "))
            if is_valid(name, salary, department_id):
                data_insert(name, salary, department_id, connection)
                print('\nEmployee data inserted')
            else:
                print('\nEmployee data not inserted')

        elif choice == 2:
            data = data_select(connection)
            print("\nEmployee | Salary | Department ID")
            for row in data:
                print(f"{row[0]:<8} | {row[1]:<6} | {row[2]}")

        elif choice == 3:
            salary = dep_salary(connection)
            output(salary)

        elif choice == 4:
            high_salaries = salary_check(connection)
            for row in high_salaries:
                print(f"{row[0]} | {row[1]} | {row[2]}")

        elif choice == 0:
            print("Exit..")
            break

        else:
            print('Wrong choice')

if __name__ == '__main__':
    main()
