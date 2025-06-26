from django.urls import path
from . import views
from django.views.generic import RedirectView
from . import api_views

urlpatterns = [
    # API views
    path('api/classes-list/', api_views.FitnessClassListAPI.as_view(), name='api-class-list'),
    path('api/book-class/', api_views.BookingAPI.as_view(), name='api-book'),
    path('api/my-bookings/', api_views.BookingByEmailAPI.as_view(), name='api-bookings-by-email'),
    
    path('', RedirectView.as_view(url='/classes/', permanent=False)), 
    
    path("classes/", views.class_list, name="class_list"),
    path("book/", views.book_class, name="book"),
    path("bookings/", views.my_bookings, name="my_bookings"),

    
]
