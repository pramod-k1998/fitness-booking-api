# 🧘‍♀️ Fitness Class Booking System (Django + DRF + Bootstrap)

This is a full-stack web application that allows users to:
- View upcoming fitness classes
- Book a class via form-based UI
- Search their bookings using email
- Access REST APIs for integration/testing

---

## 🏗 Project Architecture

| Layer        | Tech Used                | Description |
|-------------|--------------------------|-------------|
| Backend API | Django REST Framework    | Handles data validation and JSON APIs |
| UI Frontend | Django Templates + Forms | Renders pages using Bootstrap |
| Database    | SQLite (default)         | Stores classes and bookings |
| Testing     | Django TestCase + DRF    | Unit tested via API endpoints |

---

## 📂 Directory Structure

fitness_booking/
├── studio/ # Main Django app
│ ├── models.py # FitnessClass, Booking models
│ ├── serializers.py # DRF serializers (still used by API + tests)
│ ├── forms.py # Django forms (used by HTML UI)
│ ├── views.py # UI views
│ ├── urls.py # HTML routes (/classes/, /book/, /bookings/)
│ ├── templates/studio/ # Bootstrap-based HTML templates
├── fitness_booking/urls.py # Main project URLs

## 🚀 How to Run the Project

1. **Clone the repo**  
   ```bash
   git clone https://github.com/yourusername/fitness-booking-api.git
   cd fitness-booking-api

2. **Create and activate a virtual environment**  
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install requirements**  
pip install -r requirements.txt

4. **Apply migrations and load sample data**  
python manage.py migrate
python manage.py loaddata sample_data.json

5. **Run the server**  
python manage.py runserver

🌐 UI Pages (HTML)
| URL          | Description               |
| ------------ | ------------------------- |
| `/classes/`  | View all upcoming classes |
| `/book/`     | Book a class via form     |
| `/bookings/` | View bookings by email    |

📦 REST API Endpoints
| Method | Endpoint                                | Description              |
| ------ | --------------------------------------- | ------------------------ |
| GET    | `/api/classes/`                         | List all classes         |
| POST   | `/api/book/`                            | Book a class via API     |
| GET    | `/api/bookings/?email=user@example.com` | Filter bookings by email |


🧪 Running Unit Tests
Tests are written for:

    Successful booking

    Overbooking

    Duplicate booking

    Class listing

    Booking search by email

Run tests:
    python manage.py test studio

🛠 Technologies Used
    Django 3.x / 4.x

    Django REST Framework

    Bootstrap 5

    SQLite (default dev database)

👨‍💻 Author
Developed by Pramod Kumar K
LinkedIn: https://www.linkedin.com/in/pramod-kumar-k-20438214a/ 
GitHub : https://github.com/pramod-k1998