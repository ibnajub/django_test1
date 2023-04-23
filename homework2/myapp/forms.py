from django import forms


class PostForm(forms.Form):
    author = forms.CharField(label='Author', max_length=100)
    
    title = forms.CharField(label='Title', max_length=100)
    description = forms.Textarea()


class BlogpostForm(forms.Form):
    author = forms.CharField(label='Author', max_length=100)
    topic = forms.CharField(label='Topic', max_length=100)
    
    slug = forms.CharField(label='slug', max_length=100)
    title = forms.CharField(label='Title', max_length=100)
    content = forms.Textarea()
    created_at = forms.CharField(label='created_at')
    updated_at = forms.CharField(label='updated_at')
