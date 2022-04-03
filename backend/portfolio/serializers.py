from unicodedata import category
from rest_framework import serializers
from .models import ProjectCategory, Project


class ProjectSerializer(serializers.ModelSerializer):
  
  categories = serializers.SerializerMethodField('get_categories')
  key_techs = serializers.SerializerMethodField('get_key_techs')
  
  class Meta:
    model = Project
    fields = ('id', 'name', 'description', 'get_image', 'get_thumbnail', 'deployed_url', 'github_url', 'categories', 'key_techs' )

  def get_categories(self, obj):
    return [category.name  for category in obj.categories.all()]

  def get_key_techs(self, obj):
    return [tag.name  for tag in obj.tags.all()]