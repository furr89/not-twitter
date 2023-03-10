from django.contrib.auth.models import User
from django.views.generic import DetailView

from feed.models import Post

# Create your views here.
class ProfileDetailView(DetailView):

    http_method_names = ['get']
    template_name = 'profiles/detail.html'
    model = User
    context_object_name = "user"

    # Lookup user by 'username' also found in ./urls.py
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        user = self.get_object() # Will get context_object_name

        context = super().get_context_data(**kwargs)
        context['total_posts'] = Post.objects.filter(author=user).count()

        context['total_followers'] = 'TODO'

        return context
