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
│
├── manage.py
├── fitness_booking/               ← Main project config folder
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py                    ← Includes app routes
│   ├── wsgi.py
│   └── asgi.py
│
├── studio/                       
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py                  ← HTML views
│   ├── api_views.py              ← DRF views (POST, GET API)
│   ├── serializers.py            ← DRF serializers
│   ├── tests.py                  ← Updated test cases
│   ├── urls.py                   ← Includes both HTML & API routes
│   ├── templates/
│   │   └── studio/
│   │       ├── class_list.html
│   │       ├── book_form.html
│   │       └── my_bookings.html
│   └── forms.py                  ← BookingForm (used in HTML)
│
├── db.sqlite3                   
└── requirements.txt              


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
python manage.py loaddata fixtures/sample_data.json

5. **Run the server**  
python manage.py runserver

🌐 UI Pages (HTML)
| URL          | Description               |
| ------------ | ------------------------- |
| `/classes/`  | View all upcoming classes |
| `/book/`     | Book a class via form     |
| `/bookings/` | View bookings by email    |

📦 REST API Endpoints
| Method | Endpoint                                   | Description              |
| ------ | ------------------------------------------ | ------------------------ |
| GET    | `/api/classes-list/`                       | List all classes         |
| POST   | `/api/book-class/`                         | Book a class via API     |
| GET    | `/api/my-bookings/?email=user@example.com` | Filter bookings by email |


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