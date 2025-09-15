from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, ListView, DetailView
# Create your views here.
from django.forms import ModelForm
from .models import Comment

class CommentFrom(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentView(DetailView):
    model = Comment



@method_decorator(permission_required('blog.change_post'), name='post')
class CommentEditView(UpdateView, CommentView):
    fields = '__all__'

class CommentListView (ListView):
    model = Comment
