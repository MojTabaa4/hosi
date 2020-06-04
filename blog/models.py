from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

def validate_file(value):
    import  os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extentions = ['.jpg', '.png']
    if not ext.lower() in valid_extentions:
        raise ValidationError('unsupported file extention!!')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='files/user_avatar', null=False, blank=False, validators=[validate_file])
    description = models.CharField(max_length=500, null=False, blank=False)

    # def __str__(self):
    #     return self.user.first_name + " " + self.user.last_name

class Article (models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    cover = models.FileField(upload_to='files/article_avatar', null=False, blank=False, validators=[validate_file])
    content = RichTextField()
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.OneToOneField('UserProfile', on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.title

class Category (models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.FileField(upload_to='files/category_avatar', null=False, blank=False, validators=[validate_file])

    # def __str__(self):
    #     return self.title

