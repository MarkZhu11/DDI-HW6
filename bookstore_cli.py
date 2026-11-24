import sqlite3

DB_NAME = "bookstore.db"


def print_menu():
    print("\nBookstore Menu")
    print("1. View all categories")
    print("2. View all books")
    print("3. View books in a category")
    print("4. Search books by title")
    print("5. Add a new book")
    print("6. Update a book price")
    print("7. Delete a book")
    print("8. Quit")
    print("9. Search books by author")


def print_rows(rows):
    if rows:
        for row in rows:
            print(row)
    else:
        print("No results found.")


def view_categories(cursor):
    cursor.execute("SELECT categoryId, categoryName, categoryImage FROM category")
    print_rows(cursor.fetchall())


def view_books(cursor):
    cursor.execute("SELECT bookId, title, author, price, image, readNow FROM book")
    print_rows(cursor.fetchall())


def view_books_in_category(cursor):
    category_id = input("Enter a category id: ")
    cursor.execute(
        """
        SELECT book.bookId, book.title, book.author, category.categoryName
        FROM book
        JOIN category ON book.categoryId = category.categoryId
        WHERE category.categoryId = ?
        """,
        (category_id,)
    )
    print_rows(cursor.fetchall())


def search_by_title(cursor):
    keyword = input("Enter a title keyword: ")
    cursor.execute(
        "SELECT bookId, title, author, price FROM book WHERE title LIKE ?",
        ("%" + keyword + "%",)
    )
    print_rows(cursor.fetchall())


def search_by_author(cursor):
    keyword = input("Enter an author name: ")
    cursor.execute(
        "SELECT bookId, title, author, price FROM book WHERE author LIKE ?",
        ("%" + keyword + "%",)
    )
    print_rows(cursor.fetchall())


def add_book(connection, cursor):
    try:
        category_id = int(input("Enter category id: "))
        title = input("Enter title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        price = float(input("Enter price: "))
        image = input("Enter image filename: ")
        read_now = int(input("Enter readNow (0 or 1): "))

        cursor.execute(
            """
            INSERT INTO book (categoryId, title, author, isbn, price, image, readNow)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (category_id, title, author, isbn, price, image, read_now)
        )
        connection.commit()
        print("Book added.")
    except ValueError:
        print("Invalid input.")
    except sqlite3.IntegrityError as error:
        print("Could not add book:", error)


def update_price(connection, cursor):
    try:
        book_id = int(input("Enter book id: "))
        new_price = float(input("Enter new price: "))
    except ValueError:
        print("Invalid input.")
        return

    cursor.execute(
        "UPDATE book SET price = ? WHERE bookId = ?",
        (new_price, book_id)
    )
    connection.commit()
    if cursor.rowcount == 0:
        print("No book found.")
    else:
        print("Price updated.")


def delete_book(connection, cursor):
    try:
        book_id = int(input("Enter book id to delete: "))
    except ValueError:
        print("Invalid input.")
        return

    cursor.execute("DELETE FROM book WHERE bookId = ?", (book_id,))
    connection.commit()
    if cursor.rowcount == 0:
        print("No book found.")
    else:
        print("Book deleted.")


def main():
    connection = sqlite3.connect(DB_NAME)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_categories(cursor)
        elif choice == "2":
            view_books(cursor)
        elif choice == "3":
            view_books_in_category(cursor)
        elif choice == "4":
            search_by_title(cursor)
        elif choice == "5":
            add_book(connection, cursor)
        elif choice == "6":
            update_price(connection, cursor)
        elif choice == "7":
            delete_book(connection, cursor)
        elif choice == "8":
            print("Goodbye!")
            break
        elif choice == "9":
            search_by_author(cursor)
        else:
            print("Invalid option. Try again.")

    connection.close()


if __name__ == "__main__":
    main()
