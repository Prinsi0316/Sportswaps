from django.contrib import admin
from .models import CustomUser, Country, State, City, UserProfile, SportCategory, Equipment, ProductCart, Order, Payment, Feedback, ContactUs

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password', 'date_joined')

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'name')

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'state', 'name')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'dob', 'address', 'phone_no', 'image')

@admin.register(SportCategory)
class SportCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat_name', 'description')

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'category', 'price', 'description', 'stock', 'image')

@admin.register(ProductCart)
class ProductCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'plant', 'price', 'quantity', 'order_id', 'order_status')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'plant', 'quantity', 'total_price', 'order_date', 'delivery_date', 'status')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'booking', 'amount', 'payment_mode', 'payment_status', 'payment_date')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'plant', 'rating', 'comment', 'review_date')

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'message', 'phone', 'created_at')
