from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Project(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(null=True, blank=True, upload_to="images",default="default.jpg")
    featured_image_1 = models.ImageField(null=True, blank=True, upload_to="images",default="default.jpg")
    exp_f1 = models.TextField(null=True, blank=True)
    featured_image_2 = models.ImageField(null=True, blank=True, upload_to="images",default="default.jpg")
    exp_f2 = models.TextField(null=True, blank=True)
    featured_image_3 = models.ImageField(null=True, blank=True, upload_to="images",default="default.jpg")
    exp_f3 = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=800, null=True, blank=True)
    sub_headline = models.CharField(max_length=500, null=True, default=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, null=True)
    def __str__(self):
        return self.title