from django import forms
from post.models import Post



# class TestForm(forms.Form):
#     first_name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["picture", "caption",]
        # exclude = ["user"] only specfic
