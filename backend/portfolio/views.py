from unicodedata import category
from portfolio.models import Project, ProjectCategory
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from portfolio.serializers import ProjectSerializer



# Create your views here.
@api_view(["GET"])
def get_projects(request):

  projects = Project.objects.all()

  serializer = ProjectSerializer(projects, many=True)

  return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_categories(request):

  categories = ProjectCategory.objects.all()

  data = [category.name for category in categories ]  

  return Response(data, status=status.HTTP_200_OK)