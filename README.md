# fitness-booking-api
# 🏋️ Fitness Booking API

A Django-based Booking API for a fictional fitness studio.

## 📌 Features

- View upcoming classes
- Book a class with available slots
- View all bookings by email
- Bootstrap-based UI
- Secure and modular code

## 🚀 Setup Instructions

```bash
git clone https://github.com/yourusername/fitness-booking-api.git
cd fitness-booking-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata fixtures/sample_data.json
python manage.py runserver
