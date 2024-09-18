from .models import UserPost,UserPostMedia,PostLikes,PostComment
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class UserPostCreationSerializer(ModelSerializer):

    def create(self, validated_data):

        validated_data["author"]=self.context['current_user']

        return UserPost.objects.create(**validated_data)





    class Meta:

            model=UserPost
            fields=('caption_text','location','id','is_published')


class UserMediaSerializer(ModelSerializer):

    class Meta:
        model=UserPostMedia
        fields=('media_field','sequence_index','post')


class PostMediaViewSerializer(ModelSerializer):
    class Meta:
        model=UserPostMedia
        exclude=('post',)


class PostFeedSerializer(ModelSerializer):
    UserPostCreationSerializer()

    media = PostMediaViewSerializer(many=True)

    class Meta:
        model=UserPost
        fields= '__all__'
        include=('media',)


class PostLikeCreateSerializer(ModelSerializer):

    def create(self, validated_data):
        validated_data["liked_by"]=self.context['current_user']

        return PostLikes.objects.create(**validated_data)

    class Meta:
        model = PostLikes
        fields = ('post','id')


class PostCommentCreateSerializer(ModelSerializer):

    def create(self, validated_data):
        validated_data["author"] = self.context['current_user']

        return PostComment.objects.create(**validated_data)

    class Meta:
        model= PostComment
        fields= ('text', 'post','id')