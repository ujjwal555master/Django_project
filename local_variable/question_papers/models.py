from django.db import models
from django.conf import settings


# Create your models here.
class QuestionPaper(models.Model):
    title = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    exam_type = models.CharField(max_length=100, choices=[('Semester', 'Semester'), ('Competitive', 'Competitive')])
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='question_papers/')

    def __str__(self):
        return f"{self.title} ({self.exam_type})"
