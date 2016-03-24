from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    rating = models.FloatField()
    amount = models.IntegerField()
    description = models.TextField()
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
    )

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


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
    price = models.IntegerField()
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
    )

    def __str__(self):
        return self.title


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


class Cart(models.Model):
    price = models.IntegerField()
    amount = models.IntegerField()
    items = models.ManyToManyField(
        'Item',
        through='CartItem',
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


class Guest(models.AnonymousUser):
    cart = models.ForeignKey(
        'Cart',
        on_delete=models.CASCADE,
    )


class ShopUser(models.AbstractBaseUser):
    username = models.CharField(max_length=40, unique=True)
    USERNAME_FIELD = 'username'
    bill = models.IntegerField()
    discount = models.IntegerField()
    cart = models.ForeignKey(
        'Cart',
        on_delete=models.CASCADE,
    )
    laid_off = models.ForeignKey(
        'Cart',
        on_delete=models.SET_NULL,
        null=True,
    )
    orders = models.ManyToManyField(
        'Order',
    )
