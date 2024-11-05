from django import forms

from news.models import Category, Tag, News


# class NewsForm(forms.Form):
#     name = forms.CharField(label='Название', max_length=100,
#                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'News 1'}))
#     image = forms.ImageField(label='Изображение', widget=forms.FileInput(attrs={'class': 'form-control'}))
#     description = forms.CharField(label='Описание', max_length=200,
#                                   widget=forms.Textarea(attrs={'class': 'form-control', 'row': 8}))
#     content = forms.CharField(label='Контент', widget=forms.Textarea(attrs={'class': 'form-control', 'row': 8}))
#     author = forms.CharField(label='Автор', max_length=100,
#                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descrtip...'}))
#     category = forms.ModelChoiceField(label='Категорие', empty_label='Select category', queryset=Category.objects.all(),
#                                       widget=forms.Select(attrs={'class': 'form-select'}))
#     is_published = forms.BooleanField(label='Публичность', initial=False, widget=forms.CheckboxInput())
#     tags = forms.ModelMultipleChoiceField(label='Теги', queryset=Tag.objects.all(),
#                                           widget=forms.CheckboxSelectMultiple())


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = (
            'name',
            'image',
            'description',
            'content',
            'author',
            'category',
            'is_published',
            'tags',
        )

        # exclude = ('views', 'tags')

        # fields = '__all__'

        # labels = {
        #     'name': 'Название 2',
        # }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'News 1'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'row': 8}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'row': 8}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author...'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'tags': forms.CheckboxSelectMultiple(),
        }

