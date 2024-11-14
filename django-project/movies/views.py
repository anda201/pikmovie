import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import BookListSerializer, BookSerializer
from .models import Book
# import json

from django.shortcuts import render

API_URL = 'https://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = 'ttbdksekwjd3121150001'

# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):
    params = {
        'ttbkey': API_KEY,
        'QueryType': 'Bestseller',
        'MaxResults': '50',
        'start': '1',
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101'
    }
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # API 호출 오류 처리
        data = response.json()
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    books = []  # 저장된 책 정보를 담을 리스트
    response = requests.get(API_URL, params=params).json()
    
    for item in response['item']:
        book_data = {
            'title': item['title'],
            'pubDate': item['pubDate'],
            'author': item['author'],
            'bestDuration': item.get('bestDuration')
        }
        serializer = BookSerializer(data = book_data)
        if serializer.is_valid():
            serializer.save()
            books.append(serializer.data)
        else:
            Response({"error": "잘못된 데이터", "details": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(books, status=status.HTTP_201_CREATED)
    # json_val = json.dumps(response['item'])
    # print(json_val)

    
    
