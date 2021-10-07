from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),

    path('books/', views.getBooks, name="books"),
    path('books/<str:pk>', views.getBook, name="book"),

    path('book/create/', views.createBook, name="create_book"),
    path('book/update/<str:pk>', views.updateBook, name="update_book"),
    path('book/delete/<str:pk>', views.deleteBook, name="delete_book"),
]