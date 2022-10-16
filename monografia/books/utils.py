from django.conf import settings
from django.core.paginator import Paginator


def pagination(request, books):
    paginator = Paginator(books, settings.SORT10)
    return paginator.get_page(request.GET.get('page'))
