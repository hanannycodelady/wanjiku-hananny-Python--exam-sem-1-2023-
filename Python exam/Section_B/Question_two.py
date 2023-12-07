#Question_two (i)
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")


#instance
my_book = Book("The contagion ", "Wanjiku hananny", 247)


my_book.display_info()

#(ii)
class EBook(Book):
    def __init__(self, title, author, pages, format):
        super().__init__(title, author, pages)
        self.format = format

    def display_info(self):
        super().display_info()
        print(f"Format: {self.format}")
my_ebook = EBook(" contagion 2023", "M.henry", 22, "PDF")
my_ebook.display_info()

#(iii)

def get_title_author(self):
        return f"{self.title} by {self.author}"

my_book = Book("contagion", "Wanjiku hananny", 247)
my_book.display_info()
title_author = my_book.get_title_author( 'maina wasswa')
print(title_author)


#(iv)
#class starts with capital letter and is singular.

#object 
#