from django.shortcuts import render, redirect
from .models import Fitness, Booking
from .forms import BookingForm
from django.contrib import messages
from django.utils.timezone import localtime
import pytz

# Create your views here.
def class_list(request):
    classes = Fitness.objects.all()
    for cls in classes:
        cls.datetime_ist = localtime(cls.datetime, pytz.timezone("Asia/Kolkata")).strftime("%Y-%m-%d %H:%M")
    return render(request, "studio/class_list.html", {"classes": classes})


def book_class(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            fitness_class = form.cleaned_data["fitness_class"]
            client_email = form.cleaned_data["client_email"]

            if Booking.objects.filter(fitness_class=fitness_class, client_email=client_email).exists():
                messages.error(request, "You have already booked this class.")
            elif fitness_class.available_slots <= 0:
                messages.error(request, "No slots left for this class.")
            else:
                Booking.objects.create(
                    fitness_class=fitness_class,
                    client_name=form.cleaned_data["client_name"],
                    client_email=client_email
                )
                fitness_class.available_slots -= 1
                fitness_class.save()
                messages.success(request, "Booking successful!")
                return redirect("book")
    else:
        class_id = request.GET.get("class_id")
        form = BookingForm(initial={"fitness_class": class_id} if class_id else None)
    return render(request, "studio/book_form.html", {"form": form})


def my_bookings(request):
    bookings = []
    email = request.GET.get("email")
    if email:
        bookings = Booking.objects.filter(client_email=email).select_related("fitness_class")
    return render(request, "studio/my_bookings.html", {"bookings": bookings, "email": email})