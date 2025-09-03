class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            pass
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            pass
        else:
            self._name = value

    def articles(self):
        from article import Article
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        from article import Article
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list(set(article.magazine.category for article in self.articles()))
