from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.serializers import PostSerializer
from api.models import Post


class PostViewSet(viewsets.ModelViewSet):
    """
     API endpoint that allows users to be viewed or edited.
    """
    queryset = Post.objects.all().order_by('-date_time')
    serializer_class = PostSerializer

    @action(detail=False)
    def boast(self, request):
        boast = Post.objects.filter(choice="BO")
        serializer = self.get_serializer(boast, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def roast(self, request):
        roast = Post.objects.filter(choice="RO")
        serializer = self.get_serializer(roast, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def LikeView(self, request, pk=None):
        post = Post.objects.get(id=pk)
        post.up_votes += 1
        post.save()
        return Response({'status': 'post liked'})

    @action(detail=True, methods=['get'])
    def DislikeView(self, request, pk=None):
        post = Post.objects.get(id=pk)
        post.down_votes += 1
        post.save()
        return Response({'status': 'post disliked'})
