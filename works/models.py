from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)

    def __str__(self):
        return '{}'.format(self.name)

    def get_projects(self):
        return Project.objects.filter(category=self)


class Project(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    content = models.TextField(blank=False, null=False)
    image1 = models.ImageField(null=False, blank=False,upload_to='works/project',)
    image2 = models.ImageField(null=False, blank=True,upload_to='works/project')
    image3 = models.ImageField(null=False, blank=True, upload_to='works/project')

    def __str__(self):
        return '{}'.format(self.name)

