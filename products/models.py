from datetime import datetime
from django.db import models
from datetime import datetime
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=4,decimal_places=2 )
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    active = models.BooleanField(default=True)
    publish_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering =['-publish_date']    