from django.contrib.auth.models import Permission
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User


@receiver(post_save, sender=User)
def create_user_permission(sender, instance, created, **kwargs):
    permission1 = Permission.objects.get(name='Can view movie')
    permission2 = Permission.objects.get(name='Can view genre')
    permission3 = Permission.objects.get(name='Can view poster')
    u = User.objects.get(username=instance)
    u.user_permissions.add(permission1,permission2,permission3)
