# Django Login System - README

## **Project Description**

This Django project implements a login system, "Loginify," that includes CRUD (Create, Read, Update, Delete) operations for user management. It provides features for creating, retrieving, updating, and deleting user details through API endpoints. The project also utilizes Django's admin interface and is tested thoroughly using Postman.

---

## **Project Setup**

### **1. Virtual Environment**

- Create a virtual environment:
  ```bash
  python -m venv DjangoAssignment
  ```
- Activate the virtual environment:
  - Windows:
    ```bash
    DjangoAssignment\Scripts\activate
    ```
  - macOS/Linux:
    ```bash
    source DjangoAssignment/bin/activate
    ```
- Install Django:
  ```bash
  pip install django
  ```

### **2. Create Django Project**

- Create a new Django project named "Login System":
  ```bash
  django-admin startproject Login_System
  ```

### **3. Create Django Application**

- Create an app named "Loginify":
  ```bash
  python manage.py startapp Loginify
  ```

---

## **Models**

The `UserDetails` model includes the following fields:

- **username**: Primary key (CharField, max length 50)
- **email**: Unique field (EmailField)
- **password**: CharField (max length 12)

---

## **Views and Endpoints**

The application provides the following CRUD views:

### **1. Create User**

- **Endpoint**: `/api/create/`
- **Method**: POST
- **Description**: Creates a new user.
- **Fields**:
  - `username`
  - `email`
  - `password`

### **2. Get All Users**

- **Endpoint**: `/api/users/`
- **Method**: GET
- **Description**: Retrieves and displays details of all users.

### **3. Get User by Email**

- **Endpoint**: `/api/user/<email>/`
- **Method**: GET
- **Description**: Retrieves a specific user's details based on their email.

### **4. Update User**

- **Endpoint**: `/api/update/<email>/`
- **Method**: POST
- **Description**: Updates a user's username and/or password.

### **5. Delete User**

- **Endpoint**: `/api/delete/<email>/`
- **Method**: DELETE
- **Description**: Deletes a user based on their email.

---

## **URLs Configuration**

Ensure `Loginify/urls.py` contains:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_user, name='create_user'),
    path('users/', views.get_all_users, name='get_all_users'),
    path('user/<str:email>/', views.get_user_by_email, name='get_user_by_email'),
    path('update/<str:email>/', views.update_user, name='update_user'),
    path('delete/<str:email>/', views.delete_user, name='delete_user'),
]
```

Include these URLs in the project's main `urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    path('api/', include('Loginify.urls')),
]
```

---

## **Admin Configuration**

- Create a superuser to access the Django admin interface:
  ```bash
  python manage.py createsuperuser
  ```
- Verify user creation and management through the admin panel at `/admin/`.

---

## **Testing the API with Postman**

### **1. Create User**

- **URL**: `http://127.0.0.1:8000/api/create/`
- **Method**: POST
- **Body (form-data)**:
  - `username`: `example_user`
  - `email`: `user@example.com`
  - `password`: `example123`

### **2. Get All Users**

- **URL**: `http://127.0.0.1:8000/api/users/`
- **Method**: GET

### **3. Get User by Email**

- **URL**: `http://127.0.0.1:8000/api/user/user@example.com/`
- **Method**: GET

### **4. Update User**

- **URL**: `http://127.0.0.1:8000/api/update/user@example.com/`
- **Method**: POST
- **Body (form-data)**:
  - `username`: `new_example_user`
  - `password`: `newpassword456`

### **5. Delete User**

- **URL**: `http://127.0.0.1:8000/api/delete/user@example.com/`
- **Method**: DELETE

---

## **File Structure**

```
Login_System/
|├── Loginify/
|   |├── migrations/
|   |├── __init__.py
|   |├── admin.py
|   |├── apps.py
|   |├── models.py
|   |├── views.py
|   |├── urls.py
|├── Login_System/
|   |├── __init__.py
|   |├── settings.py
|   |├── urls.py
|   |├── wsgi.py
|├── manage.py
```

---

## **Commands Summary**

- Run the server:
  ```bash
  python manage.py runserver
  ```
- Apply migrations:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```
- Access the admin panel:
  ```
  http://127.0.0.1:8000/admin/
  ```

---

## **Screenshots**

Postman:
User Signup:
![User SignUp!](files/signup.png)
All Users:
![all_users](files/all_users.png)
Search:
![search_request](files/search_by_email.png)
Update:
![update_request](files/update_by_email.png)
Delete:
![delete_request](files/del_by_email.png)
Final List of Users:
![final_all_users](files/final_users.png)

---

## **Author**

This project is developed as part of a Django CRUD operation exercise.
