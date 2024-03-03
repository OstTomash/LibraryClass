class Book:
    """A simple class to represent a book.

     This class allows users to create a book with given title and author,
     and compare books by attributes

     Attributes:
         - title (str): The title of the book
         - author (str): The author of the book

     Methods:
         - __init__(self): Initializes a new book with the given attributes
         - __eq__(self, other): Returns true if title and author are the same
         - __ne__(self, other): Returns true if title and author are not the same
         - __repr__(self): Returns a string representation of the book

     Example usage:
        >>> book1 = Book('Harry', 'Joan')
        >>> book2 = Book('Potter', 'Rouling')
        >>> book3 = Book('Harry', 'Joan')
        >>> print(book1 == book2)
        False
        >>> print(book1 != book2)
        True
        >>> print(book1 != book3)
        False
        >>> print(book1 == book3)
        True
    """
    def __init__(self, title, author):
        """Initializes a new book with the given title and author"""
        self.title = title
        self.author = author

    def __eq__(self, other):
        """Returns true if title and author are the same

        Raise:
            TypeError: 'Object must be instances of class Book'
        """
        if not isinstance(other, Book):
            raise TypeError('Object must be instances of class Book')

        return self.title == other.title and self.author == other.author

    def __ne__(self, other):
        """Returns true if title and author are not the same

        Raise:
            TypeError: 'Object must be instances of class Book'
        """
        if not isinstance(other, Book):
            raise TypeError('Object must be instances of class Book')

        return self.title != other.title and self.author != other.author

    def __repr__(self):
        return f'Book: "{self.title}" - {self.author}'


class Library:
    """A simple class to represent a list of instances "Book".

    This class is used to represent a list of books and collect them. Also, this class
    allow users to get length of list of books and get one of them by index.

    Attributes:
        - books (list): list of books

    Methods:
        - __init__(list_of_books): initialize the instance with a list of books
        - __len__(): returns amount of books in list
        - __getitem__(index): returns the special book by index

    Example usage:
        >>> b1 = Book("Title1", "Author1")
        >>> b2 = Book("Title2", "Author2")
        >>> b3 = Book("Title3", "Author3")
        >>>
        >>> library = Library([b1, b2, b3])
        >>> print(len(library))
        3
        >>> print(library[2])
        Book: "Title3" - Author3
    """
    def __init__(self, list_of_books):
        self.list_of_books = list_of_books

    def __len__(self):
        return len(self.list_of_books)

    def __getitem__(self, index):
        return self.list_of_books[index]

