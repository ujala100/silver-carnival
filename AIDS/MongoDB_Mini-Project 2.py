from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['bookstore']
books = db['inventory']

def add_book():
    title = input("Title: ")
    author = input("Author: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))
    book = {"title": title, "author": author, "price": price, "stock": stock}
    result = books.insert_one(book)
    print(f"Book added with ID: {result.inserted_id}")

def view_books():
    for book in books.find():
        print(book)

def search_books():
    keyword = input("Search by title/author: ")
    results = books.find({
        "$or": [
            {"title": {"$regex": keyword, "$options": "i"}},
            {"author": {"$regex": keyword, "$options": "i"}}
        ]
    })
    for book in results:
        print(book)

def update_book():
    book_id = input("Enter _id of the book to update: ")
    field = input("Field to update (title, author, price, stock): ")
    value = input("New value: ")
    if field in ["price", "stock"]:
        value = float(value) if field == "price" else int(value)
    result = books.update_one(
        {"_id": eval(book_id)},
        {"$set": {field: value}}
    )
    print("Book updated." if result.modified_count else "No match found.")

def delete_book():
    book_id = input("Enter _id of the book to delete: ")
    result = books.delete_one({"_id": eval(book_id)})
    print("Book deleted." if result.deleted_count else "No match found.")

def main():
    while True:
        print("\n1. Add Book\n2. View All Books\n3. Search Books\n4. Update Book\n5. Delete Book\n6. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_books()
        elif choice == "4":
            update_book()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
    client.close()