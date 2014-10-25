from django.views.generic import TemplateView, ListView, CreateView, \
    DetailView, UpdateView
from .models import Posts
from rest_framework import viewsets
from .serializers import PostsSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be added, viewed or edited.
    """
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class ListPosts(ListView):
    '''
    list blog posts
    '''

    template_name = 'posts_list.html'

    model = Posts

    context_object_name = 'posts'
