from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

class Haiku(models.Model):
    user = models.ForeignKey(User)
    text = models.TextField()
    created = models.DateTimeField(default = datetime.now)
    likes = models.IntegerField(default = 0)
    dislikes = models.IntegerField(default = 0)

    def __unicode__(self):
        return u"%s (by %s)" % (self.text, self.user.username)

    class Meta:
        get_latest_by = 'created'
        ordering = ('-created',)
