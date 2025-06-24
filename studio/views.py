from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Fitness,Booking
from .serializers import FitnessClassSerializer, BookingSerializer

# Create your views here.
@api_view(['GET'])
def get_classes(request):
    classes = Fitness.objects.all()
    serializer = FitnessClassSerializer(classes,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def book_class(request):
    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
        booking = serializer.save()

        # reduce slots
        fitness_class = booking.fitness_class
        fitness_class.available_slots -= 1
        fitness_class.save()

        return Response({"message": "Booking successful", "data": serializer.data}, status=201)
    
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_bookings_by_email(request):
    email = request.query_params.get('email')
    if not email:
        return Response({'error':'Email is required'}, status=400)
    bookings = Booking.objects.filter(client_email = email)
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)
