from pprint import pprint

from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from news.models import News, Category, Tag
from workspace.forms import NewsForm


def main(request):
    news = News.objects.all().order_by('-date')

    # search = request.GET.get('search')
    # if search:
    #     news = news.filter(name__icontains=search)

    page = request.GET.get('page', 1) or 1
    pagin = Paginator(news, 10)
    news = pagin.get_page(page)

    return render(request, 'workspace/index.html', {'news': news})


def create_news(request):
    form = NewsForm()

    if request.method == 'POST':
        form = NewsForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            news = form.save()

            messages.success(request, f'The news "{news.name}" was created successfully!')
            return redirect('/workspace/')

        messages.error(request, 'Please correct some errors!')

    return render(request, 'workspace/create_news.html', {'form': form})


def update_news(request, id):
    news = get_object_or_404(News, id=id)
    form = NewsForm(instance=news)

    if request.method == 'POST':
        form = NewsForm(data=request.POST, files=request.FILES, instance=news)
        if form.is_valid():
            news = form.save()

            messages.success(request, f'The news "{news.name}" was updated successfully!')
            return redirect('/workspace/')

        messages.error(request, 'Please correct some errors!')

    return render(request, 'workspace/update_news.html', {
        'form': form,
        'news': news,
    })


def delete_news(request, id):
    news = get_object_or_404(News, id=id)
    name = news.name
    news.delete()
    messages.success(request, f'The news "{name}" was deleted successfully!')
    return redirect('/workspace/')
