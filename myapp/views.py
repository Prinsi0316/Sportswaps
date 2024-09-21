from django.shortcuts import render
from .models import Country, State, City, UserProfile, SportCategory, Equipment, ProductCart, Order, Payment, Feedback, ContactUs

def home(request):
    return render(request, 'home.html')

def country_list(request):
    countries = Country.objects.all()
    return render(request, 'country_list.html', {'countries': countries})

def state_list(request):
    states = State.objects.all()
    return render(request, 'state_list.html', {'states': states})

def city_list(request):
    cities = City.objects.all()
    return render(request, 'city_list.html', {'cities': cities})

def userprofile_list(request):
    userprofiles = UserProfile.objects.all()
    return render(request, 'userprofile_list.html', {'userprofiles': userprofiles})

def sportcategory_list(request):
    sportcategories = SportCategory.objects.all()
    return render(request, 'sportcategory_list.html', {'sportcategories': sportcategories})

def equipment_list(request):
    equipments = Equipment.objects.all()
    return render(request, 'equipment_list.html', {'equipments': equipments})

def productcart_list(request):
    productcarts = ProductCart.objects.all()
    return render(request, 'productcart_list.html', {'productcarts': productcarts})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payment_list.html', {'payments': payments})

def feedback_list(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'feedback_list.html', {'feedbacks': feedbacks})

def contactus_list(request):
    contacts = ContactUs.objects.all()
    return render(request, 'contactus_list.html', {'contacts': contacts})
