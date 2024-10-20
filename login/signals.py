from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, BusinessProfile

@receiver(post_save, sender=User)
def create_business_profile(sender, instance, created, **kwargs):
    if created:
        # When a new User is created, automatically create an associated BusinessProfile
        BusinessProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_business_profile(sender, instance, **kwargs):
    # Ensure that when the User is saved, the BusinessProfile is also saved.
    instance.business_profile.save()
