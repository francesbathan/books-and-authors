from django.shortcuts import render, redirect
from .models import Book, Author
from django.contrib import messages

def index(request): #form to add a book & homepage
    context = {
        "books": Book.objects.all()
    }
    return render(request, 'index.html', context)

def newbook(request): #to process request to add a book onto the list beside the book form and returns error message if entry = empty
    form = request.POST
    all_errors = Book.objects.book_validator(form)
    if len(all_errors) > 0:
        for form_error in all_errors.values():
            messages.error(request, form_error)
        return redirect('/')
    Book.objects.create(title=form['book_title'], desc=form['book_desc']) 
    return redirect('/')

def authors(request): #form to add an author
    context = {
        "authors": Author.objects.all()
    }
    return render(request, 'authors.html', context)

def newauthor(request): #to process request to add an author on the author list and returns error message if entry = empty
    form = request.POST
    all_errors = Author.objects.author_validator(form)
    if len(all_errors) > 0:
        for form_error in all_errors.values():
            messages.error(request, form_error)
        return redirect('/authors')
    Author.objects.create(first_name=form['author_first'], last_name=form['author_last'], notes=form['author_notes'])
    return redirect('/authors')

def books(request, id): #book information page
    context = {
        "book": Book.objects.get(id=id),
        "authors": Author.objects.all() 
    }
    return render(request, 'book_info.html', context)

def author_info(request, id): #author info page
    context = { 
        "author": Author.objects.get(id=id),
        "books": Book.objects.all()
    }
    return render(request, 'author_info.html', context)