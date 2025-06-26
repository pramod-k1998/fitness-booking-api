from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Fitness, Booking
from .serializers import FitnessClassSerializer, BookingSerializer

class FitnessClassListAPI(APIView):
    def get(self, request):
        classes = Fitness.objects.all()
        serializer = FitnessClassSerializer(classes, many=True)
        return Response(serializer.data)

class BookingAPI(APIView):
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            fitness_class = serializer.validated_data['fitness_class']
            client_email = serializer.validated_data['client_email']

            if Booking.objects.filter(fitness_class=fitness_class, client_email=client_email).exists():
                return Response({'error': 'Duplicate booking'}, status=status.HTTP_400_BAD_REQUEST)

            if fitness_class.available_slots <= 0:
                return Response({'error': 'Class is full'}, status=status.HTTP_400_BAD_REQUEST)

            booking = Booking.objects.create(
                fitness_class=fitness_class,
                client_name=serializer.validated_data['client_name'],
                client_email=client_email
            )
            fitness_class.available_slots -= 1
            fitness_class.save()

            return Response(BookingSerializer(booking).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookingByEmailAPI(APIView):
    def get(self, request):
        email = request.GET.get("email")
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
        bookings = Booking.objects.filter(client_email=email)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)
