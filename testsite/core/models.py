from django.db import models
from django.contrib.auth.models import User
    
class data(models.Model):
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ad_title = models.CharField(max_length=25)
    ad_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField()

    def __str__(self):
        return "%s: %s" % (self.ad_title, self.ad_text)
     