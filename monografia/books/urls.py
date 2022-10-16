from django.urls import path

from books import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('create/', views.book_create, name='book_create'),
    path('books/<int:book_id>/edit/', views.book_edit, name='book_edit'),
    path(
        'books/<int:book_id>/comment/',
        views.add_comment,
        name='add_comment'
    ),
    path(
        'category/<slug:slug>/',
        views.category_books,
        name='category_page'
    ),
]
