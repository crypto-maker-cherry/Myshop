from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title}"

class Address(models.Model):
    street = models.CharField(max_length=100)
    zip_code = models.PositiveIntegerField()
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.country} - {self.city}"



class Brand(models.Model):
    title = models.CharField(max_length=50)
    logo = models.ImageField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.title}"



class product(models.Model):
    title = models.CharField(max_length= 70)
    price = models.PositiveIntegerField()
    image = models.ImageField(blank = True, upload_to = 'prodduct-img')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, related_name="products")
    description = models.TextField()
    category = models.ManyToManyField(Category)
    slug = models.SlugField(blank=True)
    is_bestseller = models.BooleanField(default=False)
    suggestions = models.ManyToManyField('self')

    def __str__(self):
        return f"{self.title}"
    

    def save(self, *args , **kwargs):
        super().save(*args, **kwargs)
        self.slug = self.id
        super().save(*args, **kwargs)
    

class Feedback(models.Model):
    name = models.CharField(max_length=70) 
    rating = models.PositiveIntegerField()
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"{self.product}-Rating{self.rating}"