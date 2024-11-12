from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404

from news.models import News


def _login_required(view_func):

    def inner(request, *args, **kwargs):

        if not request.user.is_authenticated:
            messages.warning(request, 'You are not authenticated')
            return redirect('/workspace/login')

        return view_func(request, *args, **kwargs)

    return inner


def is_owner(view_func):

    def inner(request, id, *args, **kwargs):

        news = get_object_or_404(News, id=int(id))

        if news.author != request.user:
            messages.warning(request, 'You are not the owner of this news')
            return redirect('/workspace/')

        return view_func(request, id, *args, **kwargs)

    return inner