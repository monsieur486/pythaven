from django.db import models


class Information(models.Model):
    group_id = models.CharField(max_length=200)
    artifact_id = models.CharField(max_length=200)
    project_version = models.CharField(max_length=20)
    type = models.CharField(max_length=50)
    favorite = models.BooleanField(default=False)
    java_version = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
