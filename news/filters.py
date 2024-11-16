import django_filters
from django import forms

from news.models import News, Category, Tag


class NewsFilter(django_filters.FilterSet):
    categories = django_filters.ModelMultipleChoiceFilter(field_name='category', queryset=Category.objects.all(),
                                                          widget=forms.CheckboxSelectMultiple)
    tags = django_filters.ModelMultipleChoiceFilter(widget=forms.CheckboxSelectMultiple, queryset=Tag.objects.all())
    is_published = django_filters.BooleanFilter(widget=forms.CheckboxInput)
    date = django_filters.DateTimeFilter(widget=forms.DateTimeInput(attrs={'class': 'form-control'}))

    class Meta:
        model = News
        fields = ('tags', 'is_published', 'date')
