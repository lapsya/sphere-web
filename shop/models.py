from django.db import models
from django.contrib.auth.models import AnonymousUser, AbstractUser
from django.utils import timezone

class Item(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    rating = models.FloatField()
    amount = models.IntegerField()
    description = models.TextField(default='')
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
    )
    vendor = models.ForeignKey(
        'Vendor',
        on_delete=models.SET_NULL,
        null=True,
    )
    tag = models.ManyToManyField(
        'Tag',
        blank=True,
    )

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Tag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Vendor(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Order(models.Model):
    title = models.CharField(
        max_length=255,
        default='Unnamed order',
    )
    #price = models.IntegerField()
    ship_method = models.ForeignKey(
        'ShippingMethod',
        on_delete=models.SET_NULL,
        null=True,
    )
    address = models.TextField()
    DONE = 'DN'
    SHIP = 'SH'
    PROCESS = 'PR'
    WAIT = 'WT'
    ORDER_STATUS_CHOICE = (
        (DONE, 'Completed'),
        (SHIP, 'In shipping'),
        (PROCESS, 'Being processed'),
        (WAIT, 'Awaiting at delivery'),
    )
    status = models.CharField(
        max_length=2,
        choices=ORDER_STATUS_CHOICE,
        default=PROCESS,
    )
    status_timedate = models.DateTimeField(auto_now=True)
    items = models.ManyToManyField(
        'Item',
        through='ItemOrder',
        blank=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-status_timedate']


class ItemOrder(models.Model):
    item = models.ForeignKey(
        'Item',
        on_delete=models.CASCADE,
    )
    order = models.ForeignKey(
        'Order',
        on_delete=models.CASCADE,
    )
    item_amount = models.IntegerField()


class ShippingMethod(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Shipping method'


class Cart(models.Model):
    price = models.IntegerField()
    amount = models.IntegerField()
    items = models.ManyToManyField(
        'Item',
        through='CartItem',
        blank=True
    )


class CartItem(models.Model):
    cart = models.ForeignKey(
        'Cart',
        on_delete=models.CASCADE,
    )
    item = models.ForeignKey(
        'Item',
        on_delete=models.CASCADE,
    )
    item_amount = models.IntegerField()


class Guest(AnonymousUser):
    cart = models.ForeignKey(
        'Cart',
        on_delete=models.CASCADE,
    )


class ShopUser(AbstractUser):
    birth_date = models.DateField(default=timezone.now)
    address = models.TextField(default='')
    bill = models.FloatField(default=0)
    discount = models.IntegerField(default=0)
    cart = models.ForeignKey(
        'Cart',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user_cart',
    )
    laid_off = models.ForeignKey(
        'Cart',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user_laid_off_cart',
    )
    orders = models.ManyToManyField(
        'Order',
        blank=True,
    )

    def __str__(self):
        return self.title
