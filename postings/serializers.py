from rest_framework.serializers import ModelSerializer

from .models import Posting


class PostingSerializer(ModelSerializer):
    class Meta:
        model = Posting
        fields = ["id", "title", "content", "password"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        post = Posting(**validated_data)

        post.save()
        return post
