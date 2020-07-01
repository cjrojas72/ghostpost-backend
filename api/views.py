from django.shortcuts import render, HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.serializers import PostSerializer
from api.models import Post
from django.utils.crypto import get_random_string
from api.forms import AddPostForm


def postview(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                choice=data['choice'],
                post_id=get_random_string(length=6),
                body=data['body'],
            )
            return HttpResponseRedirect('http://localhost:3000/')

    form = AddPostForm()

    return render(request, 'post.html', {"form": form})


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
        post = Post.objects.get(post_id=pk)
        post.up_votes += 1
        post.save()
        return Response({'status': 'post liked'})

    @action(detail=True, methods=['get'])
    def DislikeView(self, request, pk=None):
        post = Post.objects.get(post_id=pk)
        post.down_votes += 1
        post.save()
        return Response({'status': 'post disliked'})
