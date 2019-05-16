from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from school.models import School, SchoolSerializer
from django.db.models import Count
# Create your views here.


@api_view(['GET'])
def get_by_province(request):
    schools = School.objects.values('province').annotate(
        count=Count('province'))
    if schools is None:
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(data=schools, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_by_city(request, province):
    data = School.objects.filter(province=province)
    print(len(data))
    if len(data) == 0:
        return Response(data=[], status=status.HTTP_200_OK)
    else:
        schools = data.values('city').annotate(count=Count('city'))
        return Response(data=schools, status=status.HTTP_200_OK)
