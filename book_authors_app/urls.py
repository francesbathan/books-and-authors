from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), #add books 
    path('authors', views.authors), #add authors
    path('newauthor', views.newauthor), #process path for adding new author
    path('newbook', views.newbook), #process path for adding new book
    path('books/<int:id>', views.books), #book info
    path('author_info/<int:id>', views.author_info) #author info
]
