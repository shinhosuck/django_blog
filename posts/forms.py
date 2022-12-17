from posts.models import PostReply
from django import forms


class PostReplyForm(forms.ModelForm):
    class Meta:
        model = PostReply
        fields = ['content']