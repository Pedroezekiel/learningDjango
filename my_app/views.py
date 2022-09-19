import rest_framework.generics
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book
from .serializer import BookSerializer
from rest_framework.generics import get_object_or_404


# Create your views here.
def index(request):
    context = "zeepy"
    template = loader.get_template('index.html')
    return render(request, template, context={'name': context})
    # return render(request, 'my_app/index.html', context={'name': context})


def about(request):
    return render(request, 'my_app/about.html')


def redirect(request):
    return HttpResponseRedirect(reverse('my_app:index'))


@api_view()
def book_list(request):
    queryset = Book.objects.all()
    serializer = BookSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def book_details(request, pk):
    # book = Book.objects.get(pk=pk)
    book = get_object_or_404(Book, pk=pk)
    serializer = BookSerializer(book)

    return Response(serializer.data)


@api_view()
def publisher_list(request):
    pass


def publisher_detail(request, pk):
    pass
