from datetime import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.topic_name

class Post(models.Model):
    topic = models.ForeignKey(Topic, default = '1')
    post_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('posted_date', default = datetime.now())

    def __str__(self):
        return self.post_text

    def was_posted_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

"""
class Comment(models.Model):
    post = models.ForeignKey(Post)
    comment_text =models.CharField(max_length=200)

    def __str__(self):
        return self.comment_text
"""

#class Reply(models.Model):
#   reply = models.ForeignKey(Comment)
#    reply_text = models.CharField('reply',max_length=200)

#    def __str__(self):
#        return self.reply_text

