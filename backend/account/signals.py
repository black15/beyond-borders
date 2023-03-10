from .models import Account, Profile
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=Account)
def create_profile(sender, instance, created, **kwargs):
   if created:
      Profile.objects.create(user=instance)
