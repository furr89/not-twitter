from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post

# Create your views here.
class HomePage(ListView):
    http_method_names = ['get']
    template_name = "feed/home.html"

    # The model is Post and when using from html, will be called posts
    model = Post
    context_object_name = "posts"
    
    queryset = Post.objects.all().order_by('-id')[:30]

class PostDetailView(DetailView):
    http_method_names = ['get']
    template_name = "feed/detail.html"

    model = Post
    context_object_name = "post"

# LoginRequired.. forces authentication by redirecting user to login page if not authenticated
class CreateNewPost(LoginRequiredMixin, CreateView):
    
    template_name = "feed/create.html"
    model = Post
    fields = ['text']
    success_url = "/"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):

        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)
