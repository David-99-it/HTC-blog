from django.db import models

#все что связанно с бд

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    def __str__(self):
        return self.title