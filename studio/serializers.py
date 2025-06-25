from rest_framework import serializers
from .models import Fitness,Booking
from django.utils.timezone import localtime
import pytz

class FitnessClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fitness
        fields = '__all__'

from rest_framework import serializers
from .models import Fitness, Booking
from django.utils.timezone import localtime
import pytz

class BookingSerializer(serializers.ModelSerializer):
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
        ist = pytz.timezone('Asia/Kolkata')
        return localtime(obj.fitness_class.datetime, timezone=ist).strftime('%Y-%m-%d %H:%M:%S')

    def validate(self, data):
        fitness_class = data.get('fitness_class')
        client_email = data.get('client_email')

        if not fitness_class:
            raise serializers.ValidationError("Fitness Class is required.")

        if Booking.objects.filter(fitness_class=fitness_class, client_email=client_email).exists():
            raise serializers.ValidationError("You have already booked this class.")

        if fitness_class.available_slots <= 0:
            raise serializers.ValidationError("No slots left for this class.")
        
        return data
