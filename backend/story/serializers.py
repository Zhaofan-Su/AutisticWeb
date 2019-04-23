from rest_framework import serializers
from story.models import Story, Content


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('id', 'content')


class StorySerializer(serializers.ModelSerializer):
    contents = ContentSerializer(read_only=True, many=True)

    class Meta:
        model = Story
        fields = ('id', 'name', 'age', 'intro', 'contents')
