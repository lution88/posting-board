import os
import bcrypt

from rest_framework import status
from rest_framework.generics import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from postings.models import Posting
from postings.serializers import PostingSerializer


class PostsAPI(APIView):
    ''' POSTS 전체 API '''
    def get(self, request):
        posts = Posting.objects.all().order_by("-dt_created")
        posts_serializer = PostingSerializer(posts, many=True)
        print("2. :", posts_serializer.data)
        return Response(posts_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        post_serializer = PostingSerializer(data=request.data)

        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_200_OK)
        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostAPI(APIView):
    ''' POST 단건 API '''
    def get(self, request, post_id):
        post = get_object_or_404(Posting, id=post_id)
        post_serializer = PostingSerializer(post)

        return Response(post_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, posting_id):
        post = Posting.objects.get(id=posting_id)

        input_password = request.data['password']
        print(input_password, type(input_password))
        encoded_password = input_password.encode('utf-8')
        print(encoded_password)
        encoded_db_password = post.password.encode('utf-8')
        print(encoded_db_password)

        if not bcrypt.checkpw(encoded_password, encoded_db_password):
            return Response({"message": "잘못된 비밀번호 입니다."}, status=status.HTTP_400_BAD_REQUEST)

        post_serializer = PostingSerializer(post, data=request.data, partial=True, context={'password': input_password})
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_200_OK)
        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, posting_id):
        post = Posting.objects.get(id=posting_id)
        input_password = request.data["password"]
        print(input_password)

        if input_password == post.password:
            post.delete()
            return Response({"message": "삭제 완료"})
        return Response({"message": "비밀번호를 다시 입력해 주세요."})