from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from postings.models import Posting
from postings.serializers import PostingSerializer
from postings.pagination import PaginationHandler
from postings.utils import hashed_password


class PostPagination(PageNumberPagination):
    '''페이지네이션 기본 설정'''
    page_size = 20


class PostsAPI(APIView, PaginationHandler):
    """POSTS 전체 API"""
    # 페이지네이션 클래스 설정
    pagination_class = PostPagination

    def get(self, request):
        """게시글 목록 조회"""
        posts = Posting.objects.all().order_by("-dt_created")
        page = self.paginate_queryset(posts)
        if page is not None:
            posts_serializer = self.get_paginated_response(PostingSerializer(page, many=True).data)
        else:
            posts_serializer = PostingSerializer(posts, many=True)
        return Response(posts_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """게시글 생성"""
        post_serializer = PostingSerializer(data=request.data)

        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_200_OK)
        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostAPI(APIView):
    """POST 단건 API"""

    def get(self, request, post_id):
        """게시글 상세 조회"""
        post = get_object_or_404(Posting, id=post_id)
        post_serializer = PostingSerializer(post)

        return Response(post_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, posting_id):
        """
        게시글 수정
        - 비밀번호 확인 후 맞다면 수정 진행.
        """

        post = get_object_or_404(Posting, id=posting_id)

        input_password = request.data["password"]
        result = hashed_password(input_password, post)
        if not result:
            return Response({"message": "잘못된 비밀번호 입니다."}, status=status.HTTP_400_BAD_REQUEST)

        post_serializer = PostingSerializer(result, data=request.data, partial=True)

        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_200_OK)
        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, posting_id):
        """
        게시글 삭제
        - 비밀번호 확인 후 맞다면 삭제 진행.
        """

        post = get_object_or_404(Posting, id=posting_id)

        input_password = request.data["password"]
        result = hashed_password(input_password, post)
        if result:
            result.delete()
            return Response({"message": "삭제 완료"}, status=status.HTTP_200_OK)

        return Response(
            {"message": "잘못된 비밀번호 입니다. 삭제할 수 없습니다."}, status=status.HTTP_400_BAD_REQUEST
        )
