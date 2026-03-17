from database import create_tables
from data_layer import add_book, add_author, select_books, search_by_author

create_tables()

def main():
    while True:
        print('Welcome!')
        print('\nOptions:')
        print('1. Insert author')
        print('2. Insert book')
        print('3. View all books ')
        print('4. Search books by author')
        print('0. Exit')

        option = input('Enter your option: ')
        if option == '1':
            author_name = input('Enter author name: ')
            if add_author(author_name):
                print('Author added successfully')
            else:
                print('Author not added')


        elif option == '2':
            name = input('Enter book name: ')
            price = float(input('Enter book price: '))
            author_name = input('Enter author name: ')
            if add_book(name, price, author_name):
                print('Book added successfully')
            else:
                print('Book not added')

        elif option == '3':
            books = select_books()
            print("\nBook ID |      Book Title     |  Price  | Author")
            print("--------------------------------------------------")
            for row in books:
                print(f"{row[0]:<7} | {row[1]:<19} | {row[2]:<5}$ | {row[3]}")

        elif option == '4':
            author_name = input('Enter author name: ')
            books = search_by_author(author_name)
            print(f"\n{author_name} books:")
            print("Book ID |      Book Title     | Price")
            print("-------------------------------------")
            for row in books:
                print(f"{row[0]:<7} | {row[1]:<19} | {row[2]}$")


        elif option == '0':
            print('Goodbye...')
            break
        else:
            print('Invalid option')

if __name__ == '__main__':
    main()
