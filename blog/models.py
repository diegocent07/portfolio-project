from django.db import models
import datetime

# Create your models here.
# 
class Blog(models.Model):
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to='images/blogs')
    pubdate = models.DateTimeField()
    body = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pubdate_pretty(self):
        return self.pubdate.strftime('%B %e %Y')