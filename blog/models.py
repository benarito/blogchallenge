from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True)

    def __unicode__(self):
        return self.title
