def is_valid(name, salary, department):
    alpha = 0
    for i in name:
        if i.isalpha():
            alpha += 1
    if not alpha:
        return False

    dep = 0
    for n in department:
        if n.isalpha():
            dep += 1
    if not dep:
        return False

    if not name:
        print("Name can't be empty")
        return False

    elif (salary < 0) or (not salary):
        print("Invalid salary!")
        return False
    elif not department:
        print("Department can't be empty")
        return False
    else:
        return True
