from django.db import models

from users.models import User


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название раздела")
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name="Раздел"
    )
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    book_year = models.CharField(max_length=255, verbose_name="Год издания")
    book_author = models.CharField(
        max_length=255,
        verbose_name="Автор книги"
    )
    book_publisher = models.CharField(
        max_length=255,
        verbose_name="Издательство"
    )
    book_image = models.ImageField(
        'Картинка',
        upload_to='books/images',
        blank=True
    )
    book_file = models.FileField(
        'Файл',
        upload_to='books/files',
        blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="books",
        blank=True,
        null=True,
        verbose_name="Раздел"
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Опубликовано на сайте"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='books',
        verbose_name="Автор публикации"
    )
    last_edited = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title

    # def yearpublished(self):
    #     return self.book_year.year

class Comment(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="comments",
        blank=True,
        null=True,
        verbose_name="Пост"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        blank=True,
        null=True,
        verbose_name="Автор комментария"
    )
    text = models.TextField(verbose_name="Текст комментария")
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время публикации"
    )


