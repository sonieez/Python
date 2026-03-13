def is_valid(name, salary, department):
    if not name:
        print("Name can't be empty")
        return False
    elif salary < 0:
        print("Salary can't be negative")
        return False
    elif department < 0:
        print("Departament can't be negative")
        return False
    else:
        return True
