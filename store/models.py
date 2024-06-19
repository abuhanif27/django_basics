from django.db import models


# Create your models here.
class Promotion(models.Model):
    description = models.TextField()
    discount = models.FloatField()


class Collection(models.Model):
    title = models.CharField(max_length=100)


class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, default='-')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)


class Customer(models.Model):
    class MemberChoices(models.TextChoices):
        MEMBER_BRONZE = ('B', 'Bronze')
        MEMBER_SILVER = ('S', 'Silver')
        MEMBER_GOLD = ('G', 'Gold')

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MemberChoices.choices, default=MemberChoices.MEMBER_BRONZE)


class Order(models.Model):
    class PaymentStatusChoices(models.TextChoices):
        STATUS_PENDING = ('P', 'Pending')
        STATUS_COMPLETE = ('C', 'Complete')
        STATUS_FAILED = ('F', 'Failed')

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PaymentStatusChoices.choices,
                                      default=PaymentStatusChoices.STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
