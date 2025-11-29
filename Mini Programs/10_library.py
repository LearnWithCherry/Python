class Library:
    def __init__(self, filename='library.txt'):
        self.filename = filename

    def add_book(self, book):
        with open(self.filename, 'a') as f:
            f.write(book + '\n')

    def show_books(self):
        try:
            with open(self.filename, 'r') as f:
                books = f.readlines()
                for b in books:
                    print(b.strip())
        except FileNotFoundError:
            print("No books found!")

lib = Library()

while True:
    print("\n1. Add Book  2. Show Books  3. Exit")
    c = input("Choice: ")
    if c == '1':
        lib.add_book(input("Enter book name: "))
    elif c == '2':
        lib.show_books()
    elif c == '3':
        break
    else:
        print("Invalid choice!")
