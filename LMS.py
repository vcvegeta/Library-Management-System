#1.  Using .extend() function of the list object.      

class Library:
    def __init__(self):
        self.nobooks=0                                      # instance variables
        self.books=[]                                       # instance variables using self
    def lib_management(self, *book):                        # *args -> It accepts input in the form of Tuple with multiple values     
        self.books.extend(book)                             # .extend() adds each element from tuple to the list one by one 
        self.nobooks=len(self.books)
        print(f"The total number of books are: {self.nobooks}")   
        for each_book in self.books:        # iterable list object
            print(each_book)

library=Library()
library.lib_management("Harry Potter","Spiderman","Venom")             






#2.  Without using .extend() List function:


# class Library:
#     def __init__(self):
#         self.nobooks=0   # instance variables
#         self.books=[]    # instance variables using self
#     def lib_management(self, book):
#         self.books.append(book)  # book appended in the list 'books'
#         self.nobooks=len(self.books)
#         print(f"The total number of books are: {self.nobooks}")   
#         for each_book in self.books:        # iterable list object
#             print(each_book)

# library=Library()
# library.lib_management("Harry Potter")
# library.lib_management("Spiderman")
# library.lib_management("Venom")          
