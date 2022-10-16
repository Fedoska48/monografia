from django.forms import ModelForm

from .models import Book, Comment


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = (
            'title',
            'description',
            'category',
            'book_year',
            'book_author',
            'book_publisher',
            'book_image',
            'book_file',
        )
        help_texts = {
            'title': 'Введите название',
            'description': 'Введите описание',
            'category': 'Укажите категорию',
            'book_year': 'Укажите год издания',
            'book_author': 'Укажите автора книги',
            'book_publisher': 'Укажите издательство',
            'book_image': 'Загрузите изображение',
            'book_file': 'Загрузите файл',
        }
        labels = {
            'title': 'Название книги',
            'description': 'Описание',
            'category': 'Категория',
            'book_year': 'Год издания',
            'book_author': 'Автор книги',
            'book_publisher': 'Издательство',
            'book_image': 'Изображение',
            'book_file': 'Файл',
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        help_texts = {
            'text': 'Введите текст комментария'
        }
        labels = {
            'text': 'Комментарий'
        }
