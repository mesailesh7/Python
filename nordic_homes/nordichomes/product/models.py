# models.py is used to A model field is a data type that stores a specific type of data. Each model field represents specific data, such as numbers, dates, texts, or even relationships with other models.
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        # to categorize the field alphabetically
        ordering = ('name',)


    def __str__(self):
        return self.name


# after the model has been designed it has to be assigned to the admin.py file so that it will show up in the admin panel

# to connect the product to the category we create the foreignkey and join it and on_delete=models.Cascade is if Category gets deleted then all the products will be deleted as well
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    # so to view the latest created item we use -created_at so that it goes in descending order and the most recent one shows at top
    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

    def get_display_price(self):
        return self.price / 100

