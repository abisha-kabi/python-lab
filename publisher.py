class Publisher:
    def __init__(self, name):
        self.name = name
    def display(self):
        print("Name:",self.name)


class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author

    def display(self):
        super().display()
        print("Title:", self.title)
        print("Author:",self.author)

class Python(Book):
    def __init__(self, name, title, author, price, pages):
        super().__init__(name, title, author)
        self.price = price
        self.pages = pages

    def display(self):
        super().display()
        print("Price:",self.price)
        print("pages:",self.pages)




book = Python("abisha", "Learning Python", "James", 39.99, 350)
book.display()
