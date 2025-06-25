from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/classes/', permanent=False)), 
    
    path("classes/", views.class_list, name="class_list"),
    path("book/", views.book_class, name="book"),
    path("bookings/", views.my_bookings, name="my_bookings"),
]
