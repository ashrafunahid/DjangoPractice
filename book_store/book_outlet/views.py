from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import Http404
from django.db.models import Avg, Min, Max

# Create your views here.
def index(request):
    books = Book.objects.all().order_by("-title")
    total_books_count = books.count()
    average_rating = books.aggregate(Avg("rating"))
    min_rating = books.aggregate(Min("rating"))
    max_rating = books.aggregate(Max("rating"))

    return render(request, "book_outlet/index.html", {
        "books": books,
        "total_books_count": total_books_count,
        "average_rating": average_rating,
        "min_rating": min_rating,
        "max_rating": max_rating
    })

def book_detail(request, slug):
    # try:
    #  books = Book.objects.get(id=id)
    # except:
    #     raise Http404()
    books = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_detail.html", {
        "title": books.title,
        "author": books.author,
        "rating": books.rating,
        "is_bestselling": books.is_bestselling,
    })
