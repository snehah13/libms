# Library Management System

# List to hold book details: each book is represented as a dictionary
books = [
    {"title": "Python Programming", "author": "John Doe", "status": "available"},
    {"title": "Data Science Handbook", "author": "Jane Smith", "status": "available"},
    {"title": "Machine Learning Basics", "author": "Emily White", "status": "available"}
]

def display_books():
    """Display all books in the library"""
    if len(books) == 0:
        print("No books available in the library.")
        return
    print("\nList of Books in the Library:")
    for index, book in enumerate(books, 1):
        print(f"{index}. {book['title']} by {book['author']} - Status: {book['status']}")

def add_book():
    """Add a new book to the library"""
    title = input("\nEnter the title of the book: ")
    author = input("Enter the author's name: ")
    books.append({"title": title, "author": author, "status": "available"})
    print(f"'{title}' by {author} has been added to the library.")

def delete_book():
    """Delete a book from the library"""
    display_books()
    try:
        book_index = int(input("\nEnter the number of the book to delete: ")) - 1
        if 0 <= book_index < len(books):
            deleted_book = books.pop(book_index)
            print(f"The book '{deleted_book['title']}' by {deleted_book['author']} has been removed.")
        else:
            print("Invalid choice. No book was deleted.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def borrow_book():
    """Borrow a book from the library"""
    display_books()
    try:
        book_index = int(input("\nEnter the number of the book you want to borrow: ")) - 1
        if 0 <= book_index < len(books):
            if books[book_index]['status'] == "available":
                books[book_index]['status'] = "borrowed"
                print(f"You have successfully borrowed '{books[book_index]['title']}'.")
            else:
                print("Sorry, this book is currently borrowed.")
        else:
            print("Invalid choice. No book was borrowed.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def return_book():
    """Return a borrowed book to the library"""
    display_books()
    try:
        book_index = int(input("\nEnter the number of the book you want to return: ")) - 1
        if 0 <= book_index < len(books):
            if books[book_index]['status'] == "borrowed":
                books[book_index]['status'] = "available"
                print(f"Thank you for returning '{books[book_index]['title']}'.")
            else:
                print("This book was not borrowed.")
        else:
            print("Invalid choice. No book was returned.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def library_system():
    """Main menu to interact with the library system"""
    while True:
        print("\nLibrary Management System")
        print("1. View Books")
        print("2. Add a Book")
        print("3. Delete a Book")
        print("4. Borrow a Book")
        print("5. Return a Book")
        print("6. Exit")
        
        choice = input("Please select an option (1-6): ")
        
        if choice == "1":
            display_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Run the library system
library_system()