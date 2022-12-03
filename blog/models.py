from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title=models.CharField(max_length=20)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now())
    publish_date=models.DateTimeField(null=True,blank=True)

    def publish(self):
        self.publish_date=timezone.now()
        self.save()


    def __str__(self):
        return self.title