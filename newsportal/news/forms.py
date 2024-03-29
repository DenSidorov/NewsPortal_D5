from django.forms import ModelForm
from .models import Post, Comment


# Создаём модельную форму
class PostForm(ModelForm):
    # в класс мета, как обычно, надо написать модель, по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.

    class Meta:
        model = Post
        fields = ['author', 'categoryType', 'title', 'text']


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['text']