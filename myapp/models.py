from django.db import models

class Producttable(models.Model):
    id=models.AutoField(primary_key=True)
    Product_name=models.CharField(max_length=255)
    Product_price=models.IntegerField(default=0,blank=True)
    Product_image=models.URLField()

    def __str__(self):
        return self.Product_name
