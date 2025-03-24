
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('portfolio/', views.portfolio, name='portfolio'),  # Portfolio page
    path('booking/', views.booking_request_view, name='booking'),  # Booking page
    path('contact/', views.contact_request_view, name='contact'),  # Contact page
]
