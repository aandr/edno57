from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

class Haiku(models.Model):
    user = models.ForeignKey(User)
    text = models.TextField()

    created = models.DateTimeField(default = datetime.now())

    def __unicode__(self):
        return u"%s: %s" % (self.user.username, self.text[0:50]) 
    
    class Meta:
        ordering = ('-created', )
