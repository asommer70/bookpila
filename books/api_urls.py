from django.urls import path
from . import api_views

app_name = 'books'
urlpatterns = [
    path('books', api_views.ListCreateBook.as_view(), name="books"),
    path('books/<int:pk>', api_views.RetrieveUpdateDestroyBook.as_view(), name="book"),
]
