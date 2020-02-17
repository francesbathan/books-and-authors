from django.db import models

class BookManager(models.Manager): #validation for book entered
    def book_validator(self, post_data):
        errors = {} 
        if len(post_data['book_title']) < 1:
            errors['book_title'] = 'Please enter a title.'
        if len(post_data['book_desc']) < 1:
            errors['book_desc'] = 'Please enter a description.'
        return errors

class AuthorManager(models.Manager): #validation for author entered
    def author_validator(self, post_data):
        errors = {}
        if len(post_data['author_first']) < 1:
            errors['author_first'] = 'Please enter a first name.'
        if len(post_data['author_last']) < 1:
            errors['author_last'] = 'Please enter a last name.'
        if len(post_data['author_notes']) < 1:
            errors['author_notes'] = 'Please enter notes.'
        return errors

class Book(models.Model):
    title = models.CharField(max_length = 255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
    # authors - books per author

class Author(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    notes = models.TextField()
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
