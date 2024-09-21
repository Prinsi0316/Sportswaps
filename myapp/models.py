from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    date_joined = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    dob = models.DateField()
    address = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=15)
    image = models.URLField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcToOoJnrndFqTIcvygz9DmXfGbhxfTCxss17g&s')  # Change to URLField

    def __str__(self):
        return self.user.username

class SportCategory(models.Model):
    cat_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.cat_name

class Equipment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(SportCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='equipment_images/', blank=True, null=True)

    def __str__(self):
        return self.description

class ProductCart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    plant = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    order_id = models.CharField(max_length=100, unique=True)
    order_status = models.CharField(max_length=100)

    def __str__(self):
        return self.order_id

class Order(models.Model):
    PENDING = 'Pending'
    SHIPPED = 'Shipped'
    DELIVERED = 'Delivered'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (SHIPPED, 'Shipped'),
        (DELIVERED, 'Delivered'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    plant = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)

    def __str__(self):
        return f'Order {self.id} - {self.status}'

class Payment(models.Model):
    CREDIT_CARD = 'Credit Card'
    DEBIT_CARD = 'Debit Card'
    PAYPAL = 'PayPal'
    OTHER = 'Other'
    PAYMENT_MODE_CHOICES = [
        (CREDIT_CARD, 'Credit Card'),
        (DEBIT_CARD, 'Debit Card'),
        (PAYPAL, 'PayPal'),
        (OTHER, 'Other'),
    ]

    PENDING = 'Pending'
    COMPLETED = 'Completed'
    FAILED = 'Failed'
    PAYMENT_STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (FAILED, 'Failed'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    booking = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_mode = models.CharField(max_length=20, choices=PAYMENT_MODE_CHOICES)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default=PENDING)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Payment {self.id} - {self.payment_status}'

class Feedback(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    plant = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Feedback {self.id} by {self.user.username}'

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

