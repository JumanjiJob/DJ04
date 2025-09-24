from .models import News_post
from django.forms import ModelForm, TextInput, Textarea

class News_postForm(ModelForm):
    class Meta:
        model = News_post
        fields = ['title', 'short_description', 'text']
        widgets = {
            'title': TextInput(attrs= {'class': 'form-control', 'placeholder': 'Введите название фильма'}),
            'short_description': TextInput(attrs= {'class': 'form-control', 'placeholder': 'Краткое описание фильма'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Отзыв о фильме'}),
        }