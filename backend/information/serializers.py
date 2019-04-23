from rest_framework import serializers
from information.models import Information, Content, SubTitle, SubContent, ListContent, ListTitle


class ListContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListContent
        fields = ('id', 'content')


class ListTitleSerializer(serializers.ModelSerializer):
    contents = ListContentSerializer(read_only=True, many=True)

    class Meta:
        model = ListTitle
        fields = ('id', 'title', 'contents')


class SubContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubContent
        fields = ('id', 'content')


class SubTitleSerializer(serializers.ModelSerializer):
    contents = SubContentSerializer(read_only=True, many=True)

    class Meta:
        model = SubTitle
        fields = ('id', 'title', 'contents')


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('id', 'content')


class InformationSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(read_only=True, many=True)
    sub_titles = SubTitleSerializer(read_only=True, many=True)
    list_titles = ListTitleSerializer(read_only=True, many=True)

    class Meta:
        model = Information
        fields = ('id', 'name', 'intro', 'contents', 'sub_titles',
                  'list_titles')
