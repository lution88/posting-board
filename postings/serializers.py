import bcrypt
from rest_framework.serializers import ModelSerializer

from .models import Posting


class PostingSerializer(ModelSerializer):
    ''' 게시글 시리얼라이저 ModelSerializer 사용 '''

    class Meta:
        model = Posting
        fields = ["id", "title", "content", "password", "dt_created"]
        # 기타 옵션
        extra_kwargs = {
            "password": {
                # 쓰기 전용
                "write_only": True,
                # 에러 메세지 설정.
                "error_messages": {
                    "required": "비밀번호를 입력해주세요.",
                    "invalid": "비밀번호가 틀렸습니다. 다시 입력해주세요."
                },
            },
        }

    def create(self, validated_data):
        ''' 포스팅 생성 '''
        post = Posting(**validated_data)
        password = post.password

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        decoded_password = hashed_password.decode("utf-8")

        post.password = decoded_password
        post.save()
        return post

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == 'password':
                hashed_value = bcrypt.hashpw(value.encode('utf-8'), bcrypt.gensalt())
                decoded_password = hashed_value.decode("utf-8")

                value = decoded_password
            setattr(instance, key, value)
        instance.save()

        return instance
