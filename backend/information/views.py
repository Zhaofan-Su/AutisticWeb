from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from information.models import Information
from information.serializers import InformationSerializer


@api_view(["GET"])
def get_all_informations(request):
    informations = Information.objects.all()
    if informations is None:
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = InformationSerializer(informations, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_information_by_id(request, id):
    information = Information.objects.get(id=id)
    if information is None:
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = InformationSerializer(information)
    return Response(serializer.data, status=status.HTTP_200_OK)
