from database import get_connection

def add_author(name):
    connection = get_connection()
    cursor = connection.cursor()
    authors = check_author()
    if name in authors.keys():
        a_id = authors[name]
    else:
        max_id = max(authors.values())
        a_id = max_id+1
    try:
        cursor.execute(
            "INSERT INTO authors (a_id, a_name) VALUES (:1, :2)", (a_id, name)
        )
        connection.commit()
        return True
    except:
        return False
    finally:
        cursor.close()
        connection.close()

def add_book(name, price, author_name):
    connection = get_connection()
    cursor = connection.cursor()
    books = check_book()
    if name in books.keys():
        book_id = books[name]
    else:
        max_id = max(books.values())
        book_id = max_id+1

    authors = check_author()
    author_id = authors[author_name]

    try:
        cursor.execute(
            "INSERT INTO books (b_id, b_title, b_price, a_id) VALUES (:1, :2, :3, :4)", (book_id, name, price, author_id)
        )
        connection.commit()
        return True
    except:
        return False
    finally:
        cursor.close()
        connection.close()

def select_books():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT b_id, b_title, b_price, a_name FROM books INNER JOIN authors ON books.a_id = authors.a_id"
    )
    return cursor.fetchall()

def search_by_author(author_name):
    connection = get_connection()
    cursor = connection.cursor()
    authors = check_author()
    author_id = authors[author_name.capitalize()]
    cursor.execute(f"SELECT b_id, b_title, b_price FROM books WHERE a_id = {author_id}")
    return cursor.fetchall()

def check_author():
    connection = get_connection()
    cursor = connection.cursor()
    authors = {}
    cursor.execute(
        "SELECT * FROM authors"
    )
    for row in cursor:
        authors[row[1].strip().capitalize()] = row[0]
    return authors

def check_book():
    connection = get_connection()
    cursor = connection.cursor()
    books = {}
    cursor.execute(
        "SELECT * FROM books"
    )
    for row in cursor:
        books[row[1].strip().capitalize()] = row[0]
    return books

