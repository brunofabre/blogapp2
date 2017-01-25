from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView

# Create your views here.
from blog.models import Post


class IndexView(generic.ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'index.html'

class PostsView(generic.ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts.html'

class DetailView(generic.DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'detail.html'

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'description', 'category', 'slug', 'image']
    template_name = 'create.html'

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:posts')

index = IndexView.as_view()
posts = PostsView.as_view()
detail = DetailView.as_view()
create = PostCreateView.as_view()
delete = PostDeleteView.as_view()