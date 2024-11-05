from django.http import Http404
from django.shortcuts import render, get_object_or_404
from news.models import News, Category
from django.core.paginator import Paginator


def main(request):
    news = News.objects.filter(is_published=True).order_by('-date')

    search = request.GET.get('search')
    if search:
        news = news.filter(name__icontains=search)

    category = request.GET.get('category')
    if category:
        category = Category.objects.get(id=int(category))
        news = news.filter(category=category)

    page = request.GET.get('page', 1) or 1
    pagin = Paginator(news, 10)
    news = pagin.get_page(page)

    return render(request, 'index.html', {'news': news})


def detail_news(request, id):
    news = get_object_or_404(News, id=id)
    news.views += 1
    news.save()
    return render(request, 'detail_news.html', {'news': news})


# Create your views here.
