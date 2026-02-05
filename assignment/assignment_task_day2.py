class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display_book_details(self):
        print("the title of the book is",self.title)
        print("the author of the book is ",self.author)

class Issued_book(Book):
    def __init__(self,title,author,issued_to,issued_date):
        super().__init__(title,author)
        self.issued_to=issued_to
        self.issued_date=issued_date
    def display_issued_book_details(self):
        self.display_book_details()
        print("the book is issued to ",self.issued_to)
        print("the issued book date is ",self.issued_date)


book1=Issued_book("stranger","Dr.ramesh","john","03-01-26")
book1.display_issued_book_details()