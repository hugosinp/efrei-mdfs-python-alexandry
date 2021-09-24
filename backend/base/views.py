from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from .models import Book

from .serializer import BookSerializer

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/books/',
        '/api/books/<id>',

        '/api/book/create/',
        '/api/books/delete/<id>/',
        '/api/book/<update>/<id>',
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


@api_view(['GET', 'POST'])
def addBook(request):

    print(request.data)

    book_data = request.data
    book_serializer = BookSerializer(data=book_data)
    if book_serializer.is_valid():
        book_serializer.save()
        return JsonResponse(book_serializer.data, status=status.HTTP_201_CREATED) 
    return JsonResponse(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def updateBook(request, pk):
    try: 
        book = Book.objects.get(_id=pk)
    except Book.DoesNotExist: 
        return JsonResponse({'message': 'The book does not exist'}, status=status.HTTP_404_NOT_FOUND) 