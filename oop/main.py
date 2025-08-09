# oop/main.py
from book_class import Book

def main():
    my_book = Book("1984", "George Orwell", 1949)

    # __str__ via print()
    print(my_book)

    # __repr__ via repr()
    print(repr(my_book))

    # delete object to trigger __del__
    del my_book

if __name__ == "__main__":
    main()
