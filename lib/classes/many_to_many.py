class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        type(self).all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value_to_check):
        if not isinstance(value_to_check, str):
            raise TypeError("Your title must be a string")
        elif len(value_to_check) not in range(5, 51):
            raise ValueError("Your title must be between 5 and 50 characters")
        elif hasattr(self, "_title"):
            raise ValueError("You can't update title")
        else:
            self._title = value_to_check
        

class Author:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value_to_check):
        if not isinstance(value_to_check, str):
            raise TypeError("Your name must be a string")
        elif not len(value_to_check) > 0:
            raise ValueError("Your name must be longer than 0 characters")
        elif hasattr(self, "_name"):
            raise ValueError("You can't update name")
        else:
            self._name = value_to_check


    def articles(self):
        return [article for article in Article.all if self is article.author]

    def magazines(self):
        return list({author.magazine for author in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if self.magazines():
            return list({magazine.category for magazine in self.magazines()}) 
        else:
            None

class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        type(self).all.append(self)
    
    # NAME PROP
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("your name must be a string")
        elif not len(name) in range(2, 17):
            raise ValueError("your name must be between 2 and 16 characters")
        else:
            self._name = name
            
    # CATEGORY PROP
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if not isinstance(category, str):
            raise TypeError("your category must be a string")
        elif not len(category) > 0:
            raise ValueError("your category must be more than 0 characters")
        else:
            self._category = category
                    

    def articles(self):
        return [article for article in Article.all if self is article.magazine]

    def contributors(self):
        return list({magazine.author for magazine in self.articles()})

    def article_titles(self):
        return [article.title for article in self.articles()] if self.articles() else None

    def contributing_authors(self):
        if len(self.articles()) > 2:
            return [author for author in self.contributors()]
        else: 
            None
