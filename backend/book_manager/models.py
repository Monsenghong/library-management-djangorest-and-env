from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    def __str__(self):
        return self.first_name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    author = models.ForeignKey(Author,related_name='books',on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    

class Member(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,unique=True)
    date_of_birth = models.DateField()
    def __str__(self):
        return self.first_name

class BorroweBookBasedClass(models.Model):
    borrowing_date = models.DateField()
    due_date = models.DateField()
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    status = models.CharField(max_length=100,choices=[("RETURN", "return"),("BORROWED","borrowed")])
    def __str__(self):
        return self.status
    
    

class BorrowedBook(models.Model):

    R = "RETURN"
    B = "BORROW"
    CHOICES = [(R, "borrow"),(B, "borrow")]

    borrowing_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    status = models.CharField(max_length=100,choices=CHOICES)
    def __str__(self):
        return f'Book Name:{self.book},  Borrow date:{self.borrowing_date}, due date:{self.due_date}'
