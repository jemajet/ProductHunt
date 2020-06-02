from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=250)
    url = models.TextField()
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def short_summary(self):
        max_words = 25
        if len(self.summary.split(" ")) < max_words:
            return self.summary
        else:
            return " ".join(self.summary.split(" ")[:max_words]) + "..."

    def pub_date_pretty(self):
        return self.pub_date.strftime("%b %e %Y")

    def __str__(self):
        return self.title
