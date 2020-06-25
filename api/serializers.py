from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['post_id', 'choice', 'body',
                  'up_votes', 'down_votes', 'date_time']
