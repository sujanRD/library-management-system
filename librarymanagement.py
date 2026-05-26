class users:
    def __init__(self,name):
        self.name=name
    def show_role(self):
        print("user name:",self.name)
class student(users):
    def __init__(self, name,branch):
        super().__init__(name)
        self.branch=branch
        
    def show_role(self):
        print("student name:",self.name,",branch:",self.branch)
class teacher(users):
    def __init__(self, name,subject):
        super().__init__(name)
        self.subject=subject
    def show_role(self):
        print("teacher name:",self.name," ,subject:",self.subject)
class library:
    def __init__(self):
        self.books=['maths','english','social','science','kannada']
    def display_books(self):
        print("available books:")
        for i in range(len(self.books)):
            print(f"{i}.{self.books[i]}")
    def issue_books(self,book_issue):
        
        if book_issue in self.books:
            self.books=self.books.remove(book_issue)
            print(f"{book_issue} issued sucessfully")
        else:
            print(f"{book_issue} is not available")
    def return_book(self,book_return):
        self.book_return =book_return
       
        
        self.books.append(self.book_return)
        print("remaining books:")
        print(self.books)
        
l1=library()

s1=student('sujan','CSE')
t1=teacher('asha','maths')
user=[s1,t1]
print("------------Library Management system------------")
for u in user:
    u.show_role()
l1.display_books()
book_issue=input("enter booked needed:")
l1.issue_books(book_issue)
l1.return_book('physics')

print("----------thanks for visiting-----------")









   