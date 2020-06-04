from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=200)
    contract_start_date = models.DateField()
    create_date = models.DateTimeField()
    #주문 고객사에 대한 속성을 확보하기

    def __str__(self):
        return self.customer_name


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    create_date = models.DateTimeField()
    #제품 정보에 대한 속성을 확보하기

    def __str__(self):
        return self.product_name

class Order(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    order_date = models.DateField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.customer

