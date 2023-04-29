from django import forms

# from django.forms import Textarea

from myapp.models import Blogpost, Topic, Comment


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


class PostFormModel(forms.ModelForm):
    class Meta:
        model = Blogpost
        exclude = ['updated_at']
    
    def __init__(self, *args, **kwargs):
        disabled_fields = kwargs.get('disabled_fields', None)
        if disabled_fields is not None:
            del kwargs['disabled_fields']
        super().__init__(*args, **kwargs)
        if disabled_fields:
            for field in self.fields:
                self.fields[field].disabled = True


class TopicFormModel(forms.ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'
        widgets = {
            "content": forms.Textarea(attrs={"cols": 80, "rows": 20}),
        }
        # labels = {
        #     "name": _("Writer"),
        # }
        # help_texts = {
        #     "name": _("Some useful help text."),
        # }
        # error_messages = {
        #     "name": {
        #         "max_length": _("This writer's name is too long."),
        #     },
        # }
    
    def __init__(self, *args, **kwargs):
        disabled_fields = kwargs.get('disabled_fields')
        if disabled_fields is not None:
            del kwargs['disabled_fields']
        super().__init__(*args, **kwargs)
        if disabled_fields:
            for field in self.fields:
                self.fields[field].disabled = True


class CommentFormModel(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['blogpost', 'author', 'content', ]
    
    def __init__(self, *args, **kwargs):
        disabled_fields = kwargs.get('disabled_fields')
        if disabled_fields is not None:
            del kwargs['disabled_fields']
        super().__init__(*args, **kwargs)
        if disabled_fields:
            for field in self.fields:
                self.fields[field].disabled = True
