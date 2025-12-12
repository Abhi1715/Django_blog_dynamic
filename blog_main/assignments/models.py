from django.db import models

# Create your models here.
class About(models.Model):
    about_title = models.CharField(max_length=50)
    about_description = models.CharField(max_length=250)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.about_title
    
class Sociallinks(models.Model):
    platform = models.CharField(max_length=55)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.platform