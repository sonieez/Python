import oracledb

def get_connection():
    return oracledb.connect(
        user='enda',
        password='1401',
        dsn="localhost/orcl21c"
    )

def create_tables():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE authors(
        a_id NUMBER PRIMARY KEY,
        a_name VARCHAR2(50))
    """)
    cursor.execute("""
        CREATE TABLE books(
        b_id NUMBER PRIMARY KEY,
        b_title VARCHAR2(50),
        b_price FLOAT,
        a_id NUMBER,
        CONSTRAINT fk_a_id FOREIGN KEY (a_id)
            REFERENCES authors(a_id))
    """)

    connection.commit()
    cursor.close()
    connection.close()
