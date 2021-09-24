from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),

    path('books/', views.getBooks, name="books"),
    path('books/<str:pk>', views.getBook, name="book"),

    path('books/add/', views.addBook, name="add_book"),

    path('books/update/<str:pk>', views.updateBook, name="update_book"),
    path('books/delete/<str:pk>', views.deleteBook, name="delete_book"),
]