from django.http.response import JsonResponse
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
        '/api/books/create/',

        '/api/books/upload/',

        '/api/books/<id>/reviews/',

        '/api/books/top',
        '/api/books/<id>',

        '/api/books/delete/<id>/',
        '/api/books/<update>/<id>',
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
        return JsonResponse({'message': 'The book does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    serializer = BookSerializer(book, many=False)

    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
def deleteBook(request, pk):

    try: 
        book = Book.objects.get(_id=pk)
    except Book.DoesNotExist: 
        return JsonResponse({'message': 'The book does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    book.delete()

    return JsonResponse({'message': 'book was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def addBook(request, pk):
    pass


@api_view(['PUT'])
def updateBook(request, pk):
    pass