# AnyService Backend

The backend service for **AnyService**, a multi‑country home‑services marketplace operating in Saudi Arabia, UAE, and Egypt.  
This backend is built with **Django**, **Django REST Framework**, and **PostgreSQL**, and provides all core APIs for customers, providers, and admins.

---

## Features

### Authentication & Users
- Custom user model (customer, provider, admin roles)
- JWT authentication (login, register, refresh)
- Phone + email support

### Providers
- Provider onboarding & verification
- Service areas (cities, districts)
- Pricing per service
- Weekly commission tracking (providers pay 15% weekly)
- Rating system with minimum threshold (2.0)

### Customers
- Profile management
- Saved addresses (GPS support)
- Favourites
- Booking history

### Services
- Service categories (Cleaning, AC, Plumbing, etc.)
- Service types (e.g., Home Cleaning 3h, AC Repair)

### Bookings
- Real‑time provider acceptance flow
- Status tracking (requested → accepted → on the way → completed)
- Cancellation rules
- No‑show penalties

### Payments & Commission
- Automatic 15% commission calculation per booking
- Weekly commission owed per provider
- Payment logs

### Admin Panel
- Provider approval
- Customer management
- Booking management
- Disputes
- Analytics (countries, services, revenue)

---

## Tech Stack

- **Backend:** Django, Django REST Framework  
- **Database:** PostgreSQL  
- **Auth:** JWT (SimpleJWT)  
- **Cache / Tasks:** Redis + Celery (later)  
- **Deployment:** To be added (Docker, Render, Railway, or VPS)

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/AnyService-homes/backend.git
cd backend
```

### 2. Create backend folder
```bash
mkdir backend
cd backend
```

### 3. Create Django project
```bash
django-admin startproject config .
python manage.py startapp accounts
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Run migrations
```bash
python manage.py migrate
```

### 6. Start development server
```bash
python manage.py runserver
```

---

## Roadmap

- [ ] Custom User model

- [ ] JWT authentication

- [ ] Provider onboarding

- [ ] Service categories & types

- [ ] Booking system

- [ ] Commission system

- [ ] Ratings

- [ ] Admin dashboard

- [ ] Frontend integration
