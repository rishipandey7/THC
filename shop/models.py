from django.db import models

# Create your models here.

class Product(models.Model):

    product_ID = models.AutoField
    product_Name = models.CharField(max_length = 100)
    category = models.CharField(max_length = 50,default="")
    sub_category = models.CharField(max_length = 50,default="")
    price = models.IntegerField(default = 0)
    description = models.CharField(max_length = 200)
    publish_Date = models.DateField()
    image = models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_Name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name


class Order(models.Model):
    
    order_id = models.AutoField(primary_key=True)
    item_json = models.CharField(max_length=10000)
    amount=models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default="")
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, default="")
    zip_code= models.CharField(max_length=50, default="")

class OrderUpdate(models.Model):
    
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

    def __str__(self):
        return self.update_desc
    