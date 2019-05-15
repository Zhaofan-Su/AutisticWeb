from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from score.models import Question, QuestionSerializer
# Create your views here.


@api_view(["GET"])
def getQusetions(request):
    questions = Question.objects.all()
    if questions is None:
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = QuestionSerializer(questions, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)