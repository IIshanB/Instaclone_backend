from django.db import models

from django.contrib.auth.models import User


class Timestamp(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# user


class UserProfile(Timestamp):


    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False,related_name='profile')
    profile_pic_url = models.ImageField(upload_to='profile_pic/',blank=True)

    bio = models.CharField(max_length=255, blank=True)
    is_verified = models.BooleanField(default=True)



##Foollower Section


class NetworkEdge(Timestamp):

    from_user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='following')

    to_user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='followers')

    class Meta:
        unique_together=('from_user','to_user')

