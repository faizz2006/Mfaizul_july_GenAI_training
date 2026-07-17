# q2_library_system.py

library = {
    "Python": True,
    "Java": True,
    "C++": True,
    "AI": True
}

borrowed_books = []

while True:
    print("\n===== Library Menu =====")
    print("1. Show Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nAvailable Books:")
        for book, available in library.items():
            status = "Available" if available else "Borrowed"
            print(f"{book} - {status}")

    elif choice == "2":
        book = input("Enter Book Name: ")

        if book in library and library[book]:
            library[book] = False
            borrowed_books.append(book)
            print("Book Borrowed Successfully!")
        else:
            print("Book Not Available.")

    elif choice == "3":
        book = input("Enter Book Name: ")

        if book in borrowed_books:
            borrowed_books.remove(book)
            library[book] = True
            print("Book Returned Successfully!")
        else:
            print("Book was not borrowed.")

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")
