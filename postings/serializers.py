from rest_framework.serializers import ModelSerializer

from .models import Posting


class PostingSerializer(ModelSerializer):
    model = Posting
    fields = ['title', 'content', 'password']

    def create(self, validated_data):
        post = Posting(**validated_data)
        post.save()
        return post
