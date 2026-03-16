import oracledb

def get_connection():
    return oracledb.connect(
        user='enda',
        password='1401',
        dsn="localhost/orcl21c"
    )

def create_table():
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute('''
        CREATE TABLE employees_department (
        e_name varchar(20),
        e_salary number,
        d_name varchar(30)
        )
    ''')
    connect.commit()
    cursor.close()
    connect.close()

