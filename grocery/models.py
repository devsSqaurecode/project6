from django.db import models

# Create your models here.

GROCERY_CATEGORY = (
    ('vegetable','Vegetable'),
    ('fruit','Fruit')
)

class Company(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True,upload_to="images/comapny")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/product")
    url = models.URLField()
    categories = models.CharField(max_length=100,               choices=GROCERY_CATEGORY, default='vegetable')
    company = models.ForeignKey(Company,on_delete=models.CASCADE)

    def __str__(self):
        return 'Product {} by {}'.format(self.name,self.company)
