from django.db import models
from users.models import Timestamp , UserProfile
from.permissions import HasLikingPermission

# Create your models here.


class UserPost(Timestamp):

    caption_text = models.CharField(max_length=255,blank=True)
    location = models.CharField(max_length=255,blank=True)
    is_published= models.BooleanField(default=False)
    author=models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='post')

class UserPostMedia(Timestamp):

    media_field = models.FileField(upload_to='media/',)
    sequence_index = models.PositiveSmallIntegerField(default=0)
    post = models.ForeignKey(UserPost,on_delete=models.CASCADE,related_name='media')

    class Meta:
        unique_together=('sequence_index','post')



class PostLikes(Timestamp):

    post = models.ForeignKey(UserPost,on_delete=models.CASCADE,related_name='likes')

    liked_by= models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='liked_posts')

    class Meta:
        unique_together=('post','liked_by')


class PostComment(Timestamp):
    post = models.ForeignKey(UserPost, on_delete=models.CASCADE, related_name='comment')

    author=models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='comment_made')

    text= models.CharField(max_length=255)