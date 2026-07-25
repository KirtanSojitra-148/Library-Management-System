print("Welcome to Book module")

n = int(input("Enter number of books: "))

books = []

for i in range(n):
    print("\nEnter details of Book", i + 1)

    book = {}
    book["Book ID"] = input("Book ID: ")
    book["Title"] = input("Book Title: ")
    book["Author"] = input("Author Name: ")
    book["Publisher"] = input("Publisher: ")
    book["Category"] = input("Category: ")
    book["Price"] = float(input("Price: "))
    book["Quantity"] = int(input("Quantity: "))

    books.append(book)

print("\n------ Book Details ------")

for i in range(n):
    print("\nBook", i + 1)
    for key, value in books[i].items():
        print(key, ":", value)