from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.user.models import PFTUser, UserProfile


@receiver(post_save, sender=PFTUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
