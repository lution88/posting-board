from django.shortcuts import render
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response

from postings.models import Posting
from postings.serializers import PostingSerializer


class PostsAPI(APIView):
    def get(self, request):
        posts = Posting.objects.all()
        posts_serializer = PostingSerializer(posts, many=True)
        return Response(posts_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        post_serializer = PostingSerializer(data=request.data)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_200_OK)
        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)