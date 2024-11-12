from django import forms
from django.contrib.auth.forms import BaseUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password

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
            'category': forms.Select(attrs={'class': 'form-select'}),
            'tags': forms.CheckboxSelectMultiple(),
        }


class LoginForm(forms.Form):

    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class RegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Придумайте пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        validators=[validate_password]
    )
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        )

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите фамилию'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Придумайте имя пользователя'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите эл. почту'}),
        }

    def clean(self):
        password1 = self.cleaned_data.pop('password1')
        password2 = self.cleaned_data.pop('password2')

        if self.is_valid():

            if password1 != password2:
                raise forms.ValidationError({'password2': ['The passwords are not matched.']})

            self.cleaned_data['password'] = make_password(password1)

        return self.cleaned_data
