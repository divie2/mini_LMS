# Mini LMS Backend

This is a mini Learning Management System (LMS) backend built with Django REST Framework. It provides RESTful APIs for managing courses and enrollments with token-based authentication.

---

## **Requirements**

### **Core Features**
1. **Course Management**:
   - Create, retrieve, update, and delete courses.
2. **Enrollment Management**:
   - Enroll users in courses and list enrollments.

### **Technical Features**
- Built with **Django REST Framework**.
- Uses **SQLite** as the database.
- Token-based authentication for protected endpoints.

---

## **Endpoints**

### **Authentication**
- **Obtain Token**:
  - **POST** `https://mini-lms.onrender.com/api/token`
  - Request Body:
    ```json
    {
        "username": "your_username",
        "password": "your_password"
    }
    ```
  - Response:
    ```json
    {
        "token": "your_token_key"
    }
    ```

---

### **Course Management**
- **List All Courses**:
  - **GET** `https://mini-lms.onrender.com/courses`
  - Response:
    ```json
    [
        {
            "id": 1,
            "title": "Course 1",
            "description": "Description of Course 1",
            "price": 99.99
        }
    ]
    ```

- **Retrieve a Course**:
  - **GET** `https://mini-lms.onrender.com/courses/course_id=1&price=300`
  - Response:
    ```json
    {
        "id": 1,
        "title": "Course 1",
        "description": "Description of Course 1",
        "price": 99.99
    }
    ```

- **Create a Course**:
  - **POST** `https://mini-lms.onrender.com/courses`
  - Request Body:
    ```json
    {
        "title": "New Course",
        "description": "This is a new course.",
        "price": 99.99
    }
    ```
  - Response:
    ```json
    {
        "id": 2,
        "title": "New Course",
        "description": "This is a new course.",
        "price": 99.99
    }
    ```

- **Update a Course**:
  - **PUT** `https://mini-lms.onrender.com/courses/<id>`
  - Request Body:
    ```json
    {
        "title": "Updated Course",
        "description": "This course has been updated.",
        "price": 129.99
    }
    ```
  - Response:
    ```json
    {
        "id": 1,
        "title": "Updated Course",
        "description": "This course has been updated.",
        "price": 129.99
    }
    ```

- **Delete a Course**:
  - **DELETE** `https://mini-lms.onrender.com/courses/<id>`
  - Response: `204 No Content`

---

### **Enrollment Management**
- **List All Enrollments**:
  - **GET** `https://mini-lms.onrender.com/enrollments`
  - Response:
    ```json
    [
        {
            "id": 1,
            "user": 1,
            "course": 1
        }
    ]
    ```

- **Enroll a User in a Course**:
  - **POST** `https://mini-lms.onrender.com/enrollments`
  - Request Body:
    ```json
    {
        "course": 1
    }
    ```
  - Response:
    ```json
    {
        "id": 1,
        "user": 1,
        "course": 1
    }
    ```

- **Retrieve an Enrollment by course id or user id**:
  - **GET** `https://mini-lms.onrender.com/enrollments?course_id=1`
  - Response:
    ```json
    {
        "id": 1,
        "user": 1,
        "course": 1
    }
    ```


## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```
### **Access the API**
   -The API is hosted at: https://mini-lms.onrender.com.

   -Use tools like Postman or cURL to interact with the API.

   -For protected endpoints, include the token in the Authorization header:
      **Authorization**: Token your_token_key
   
###
