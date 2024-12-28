from django.db import models
from communities.models import Community 
from django.conf import settings
# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    event_date = models.DateField()
    posted_by = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class New(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='news')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='news_posts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
