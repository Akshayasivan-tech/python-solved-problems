class Book:
    def_init_(self,title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def__str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
book=Book("1984", "George Orwell", 1949)        
print(book)