from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


# Create your views here.
from blog.models import Post


User = get_user_model()


class IndexView(generic.ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'index.html'


class PostsView(LoginRequiredMixin, generic.ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts.html'


class DetailView(generic.DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'detail.html'


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ['title', 'description', 'category', 'slug', 'image']
    template_name = 'create.html'


class PostEditView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    fields = ['title', 'description', 'category', 'slug', 'image']
    template_name = 'edit.html'


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy('blog:posts')


index = IndexView.as_view()
posts = PostsView.as_view()
detail = DetailView.as_view()
create = PostCreateView.as_view()
edit = PostEditView.as_view()
delete = PostDeleteView.as_view()
