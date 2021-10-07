from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Book

from .serializer import BookSerializer

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/books/',
        '/api/books/<id>',

        '/api/book/create/',
        '/api/book/delete/<id>/',
        '/api/book/update/<id>',
    ]

    return Response(routes)


@api_view(['GET'])
def getBooks(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getBook(request, pk):

    try: 
        book = Book.objects.get(_id=pk)
    except Book.DoesNotExist: 
        return Response({'message': 'The book does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    serializer = BookSerializer(book, many=False)

    return Response(serializer.data)


@api_view(['GET', 'POST'])
def createBook(request):

    print(request.data)

    book_data = request.data
    book_serializer = BookSerializer(data=book_data)
    if book_serializer.is_valid():
        book_serializer.save()
        return Response(book_serializer.data, status=status.HTTP_201_CREATED) 
    return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def updateBook(request, pk):
    try: 
        book = Book.objects.get(_id=pk)
        book_data = request.data
        book_serializer = BookSerializer(book, data=book_data)

        if book_serializer.is_valid():
            book_serializer.save()
            return Response(book_serializer.data, status=status.HTTP_201_CREATED)

    except: 
        return Response("The book does not exist", status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'DELETE'])
def deleteBook(request, pk):

    try: 
        book = Book.objects.get(_id=pk)
    except Book.DoesNotExist: 
        return Response("The book does not exist", status=status.HTTP_404_NOT_FOUND) 

    book.delete()

    return Response("Book was successfully deleted!", status=status.HTTP_204_NO_CONTENT)
