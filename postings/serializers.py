from rest_framework.serializers import ModelSerializer

from .models import Posting


class PostingSerializer(ModelSerializer):
    class Meta:
        model = Posting
        fields = ["id", "title", "content", "password", "dt_created"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        post = Posting(**validated_data)
        password = post.password
        post.save()
        return post
