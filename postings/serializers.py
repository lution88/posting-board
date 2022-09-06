from rest_framework.serializers import ModelSerializer

from .models import Posting


class PostingSerializer(ModelSerializer):
    ''' 게시글 시리얼라이저 ModelSerializer 사용 '''
    class Meta:
        # 사용 모델
        model = Posting
        # 사용 필드들
        fields = ["id", "title", "content", "password", "dt_created"]
        # 기타 옵션
        extra_kwargs = {
            "password": {
                # 쓰기 전용
                "write_only": True,
                # 에러 메세지 설정.
                "error_message": {
                    "required": "비밀번호를 입력해주세요.",
                    "invalid": "비밀번호가 틀렸습니다. 다시 입력해주세요."
                },
            },
        }

    def create(self, validated_data):
        post = Posting(**validated_data)
        password = post.password
        post.save()
        return post

