from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from story.serializers import StorySerializer, ContentSerializer
from story.models import Story, Content


@api_view(["GET"])
def get_all_stories(request):
    stories = Story.objects.all()
    serializer = StorySerializer(stories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def search_by_id(request):
    story_id = request.data['id']
    story = Story.Objects.get(id=story_id)
    if story is None:
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = StorySerializer(story)
    return Response(serializer.data, status=status.HTTP_200_OK)
