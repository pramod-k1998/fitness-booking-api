from rest_framework import serializers
from .models import Fitness,Booking
from django.utils.timezone import localtime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pytz

class FitnessClassSerializer(serializers.ModelSerializer):
    """
    Serializer for the Fitness model.
    Used to serialize all fields of a fitness class.
    """
    class Meta:
        model = Fitness
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for creating and viewing Booking instances.
    Includes additional read-only fields for displaying class details.
    Validates duplicate bookings and full class capacity.
    """
    fitness_class_name = serializers.CharField(source='fitness_class.name', read_only=True)
    instructor = serializers.CharField(source='fitness_class.instructor', read_only=True)
    available_slots = serializers.IntegerField(source='fitness_class.available_slots', read_only=True)
    datetime = serializers.DateTimeField(source='fitness_class.datetime', read_only=True)
    datetime_ist = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = [
            'id',
            'fitness_class',
            'fitness_class_name',
            'instructor',
            'available_slots',
            'datetime',
            'datetime_ist',
            'client_name',
            'client_email',
            'booked_at',
        ]

    def get_datetime_ist(self, obj):
        """
        Converts UTC datetime to Asia/Kolkata timezone for display.
        """
        ist = pytz.timezone('Asia/Kolkata')
        return localtime(obj.fitness_class.datetime, timezone=ist).strftime('%Y-%m-%d %H:%M:%S')

    def validate(self, data):
        """
        Validates the Booking:
        - Fitness class must exist
        - Booking must not be duplicated by email
        - Class must have available slots
        """
        fitness_class = data.get('fitness_class')
        client_email = data.get('client_email')

        if not fitness_class:
            raise serializers.ValidationError("Fitness Class is required.")

        if Booking.objects.filter(fitness_class=fitness_class, client_email=client_email).exists():
            raise serializers.ValidationError("You have already booked this class.")

        if fitness_class.available_slots <= 0:
            raise serializers.ValidationError("No slots left for this class.")
        
        return data

class BookingAPI(APIView):
    """
    POST /api/book/

    Creates a new booking for a fitness class if:
    - The class exists
    - The class has available slots
    - The user hasn't already booked the class
    """
    def post(self, request):
        """Handles POST request to book a class."""
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            booking = serializer.save()
            return Response(BookingSerializer(booking).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)