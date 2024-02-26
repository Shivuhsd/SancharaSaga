from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name = 'home'),
    path('userbooking/', views.UserBooking.as_view(), name='userbooking'),
    path('feedback/', views.Feedback.as_view(), name="feedback"),
]