from django.views.generic import UpdateView, ListView
# Create your views here.
from django.forms import ModelForm
from .models import Comment

class CommentFrom(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentView (UpdateView):
    model = Comment
    fields = '__all__'

class CommentListView (ListView):
    model = Comment
