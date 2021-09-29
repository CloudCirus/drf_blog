from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer


# порядок наследования важен
class PostSerialazer(TaggitSerializer, serializers.ModelSerializer):

    tags = TagListSerializerField()
    author = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Post
        fields = ('id', 'h1', 'title', 'slug', 'description',
                  'content', 'image', 'created_at', 'author', 'tags')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
