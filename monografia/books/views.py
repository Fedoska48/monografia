from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect

from .forms import BookForm, CommentForm
from .models import Book, User, Category
from .utils import pagination


def index(request):
    books = Book.objects.select_related('category', 'author').all()
    page_obj = pagination(request, books)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'books/index.html', context)


def category_books(request, slug):
    category = get_object_or_404(Category, slug=slug)
    books = category.books.select_related('category').all()
    page_obj = pagination(request, books)
    context = {
        'category': category,
        'page_obj': page_obj,
    }
    return render(request, 'books/category_page.html', context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    books = author.books.select_related('category').all()
    page_obj = pagination(request, books)
    context = {
        'page_obj': page_obj,
        'author': author,
    }
    return render(request, 'books/profile.html', context)


def book_detail(request, book_id):
    book = get_object_or_404(
        Book.objects.select_related('author').prefetch_related(
            'comments__author'), id=book_id
    )
    form = CommentForm(
        request.POST or None,
        files=request.FILES or None
    )
    context = {
        'book': book,
        'form': form,
        'comments': book.comments.all()
    }
    return render(request, 'books/book_detail.html', context)


@login_required
def book_create(request):
    form = BookForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        new_book = form.save(commit=False)
        new_book.author = request.user
        new_book.save()
        return redirect('books:book_detail', book_id=new_book.id)
    context = {
        'form': form
    }
    return render(request, 'books/create_book.html', context)


@login_required
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.user != book.author:
        return redirect('books:book_detail', book_id=book_id)
    form = BookForm(
        request.POST or None,
        files=request.FILES or None,
        instance=book
    )
    if form.is_valid():
        form.save()
        return redirect('books:book_detail', book_id=book_id)
    context = {
        'form': form,
    }
    return render(request, 'books/create_book.html', context)


@login_required
def add_comment(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    form = CommentForm(
        request.POST or None,
    )
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.book = book
        comment.save()
    return redirect('books:book_detail', book_id=book_id)
