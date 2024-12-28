from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    uploaded_by = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    file = models.FileField(upload_to='notes/')
    tags = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
