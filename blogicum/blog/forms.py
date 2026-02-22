from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'pub_date', 'category', 'location', 'image']
        widgets = {
            'pub_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'text': forms.Textarea(attrs={'rows': 5}),
        }
        labels = {
            'title': 'Заголовок',
            'text': 'Текст публикации',
            'pub_date': 'Дата и время публикации',
            'category': 'Категория',
            'location': 'Местоположение',
            'image': 'Изображение',
        }
        help_texts = {
            'pub_date': 'Можно отложить отправку до нужного времени',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Ваш комментарий...'}),
        }
        labels = {
            'text': 'Комментарий',
        }
