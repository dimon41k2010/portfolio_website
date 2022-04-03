from django.db import models
from PIL import Image
from io import BytesIO

from django.core.files import File


# Create your models here.

class ProjectCategory(models.Model):
  name = models.CharField(max_length=100)
  
  def __str__(self):
    return self.name

class ProjectTag(models.Model):
  name = models.CharField(max_length=100)
  
  def __str__(self):
    return self.name

class Project(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(blank=True, null=True)
  image = models.ImageField(upload_to='uploads/', blank=True, null=True)
  thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
  deployed_url = models.CharField(max_length=300, blank=True, null=True)
  github_url = models.CharField(max_length=300, blank=True, null=True)
  categories = models.ManyToManyField(ProjectCategory)
  tags = models.ManyToManyField(ProjectTag)
  date_added = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ('-date_added',)

  def __str__(self):
    return self.name

  def get_image(self):
    if self.image:
      return 'http://127.0.0.1:8000' + self.image.url
    return ''

  def get_thumbnail(self):
    if self.thumbnail:
      return 'http://127.0.0.1:8000' + self.thumbnail.url
    else:
      if self.image:
        self.thumbnail = self.make_thumbnail(self.image)
        self.save()

        return 'http://127.0.0.1:8000' + self.thumbnail.url
      else:
        return ''

  def make_thumbnail(self, image, size=(300,200)):
    img = Image.open(image)
    img.convert('RGB')
    img.thumbnail(size)

    thumb_io = BytesIO()
    img.save(thumb_io, 'JPEG', quality=85)

    thumbnail = File(thumb_io, name=image.name)

    return thumbnail
