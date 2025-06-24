from rest_framework import serializers
from .models import Fitness,Booking

class FitnessClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fitness
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    
