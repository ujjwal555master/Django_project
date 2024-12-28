from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Notification
from notes.models import Note
from question_papers.models import QuestionPaper
from projects.models import Project

# Signal for new note creation
@receiver(post_save, sender=Note)
def notify_new_note(sender, instance, created, **kwargs):
    print(f"Signal fired for project update: {instance.title}")
    if created:
        print(f"Signal fired for project update: {instance.title}")
        message = f"New note added in your community: {instance.title}"
        users_to_notify = get_user_model()  # Get users in the community
        for user in users_to_notify:
            Notification.objects.create(user=user, message=message)

# Signal for new question paper creation
@receiver(post_save, sender=QuestionPaper)
def notify_new_question_paper(sender, instance, created, **kwargs):
    if created:
        message = f"New question paper uploaded for {instance.subject} in your community."
        users_to_notify = get_user_model()  # Get users in the community
        for user in users_to_notify:
            Notification.objects.create(user=user, message=message)

# Signal for project update
@receiver(post_save, sender=Project)
def notify_project_update(sender, instance, created, **kwargs):
    if not created:  # If the project was updated
        message = f"Your project '{instance.title}' has been updated."
        participants = get_user_model()
        for user in participants:
            Notification.objects.create(user=user, message=message)
