from django.db import models

# Create your models here.
class ProjectIdea(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    interested_users = models.ManyToManyField('accounts.CustomUser', related_name='interested_projects', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class ProjectIdeas(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
