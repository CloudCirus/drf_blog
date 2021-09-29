# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerialazer
from .models import Post
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerialazer
    queryset = Post.objects.all()
    lookup_field = 'slug'
