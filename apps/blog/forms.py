from django import forms
from apps.blog.models import Post, Comment


class PostCreateForm(forms.ModelForm):
    """
    Форма добавления статей на сайте
    """

    class Meta:
        model = Post
        fields = ('title', 'category', 'description', 'text', 'thumbnail', 'status')

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы под Bootstrap
        """
        super(PostCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})

        self.fields['description'].widget.attrs.update({'class': 'form-control django_ckeditor_5'})
        self.fields['text'].widget.attrs.update({'class': 'form-control django_ckeditor_5'})


class PostUpdateForm(forms.ModelForm):
    """
    Форма обновления статьи на сайте
    """

    class Meta:
        model = Post
        fields = PostCreateForm.Meta.fields + ('fixed',)

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы под Bootstrap
        """
        super(PostUpdateForm, self).__init__(*args, **kwargs)
        self.fields['fixed'].widget.attrs.update({'class': 'form-check-input'})


class CommentCreateForm(forms.ModelForm):
    """
    Форма добавления комментариев к статьям
    """
    parent = forms.IntegerField(widget=forms.HiddenInput, required=False)
    content = forms.CharField(label='', widget=forms.Textarea(
        attrs={'cols': 30, 'rows': 5, 'placeholder': 'Комментарий', 'class': 'form-control'}))

    class Meta:
        model = Comment
        fields = ('content',)
