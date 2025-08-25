class Article:
    all = []

    def __init__(self, author, magazine, title):
        from lib.author import Author
        from lib.magazine import Magazine
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author.")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of Magazine.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        from lib.author import Author
        if not isinstance(value, Author):
            raise TypeError("Author must be an instance of Author.")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        from lib.magazine import Magazine
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be an instance of Magazine.")
        self._magazine = value
