
# Idealog – Django Idea Management System

Idealog is a Django-based web application that allows users to submit, manage, and track innovative ideas.  
It includes user authentication, admin workflows, idea status tracking, and a clean UI for managing ideas efficiently.


## 📌 Features

✔ User Registration & Login  
✔ Submit new ideas  
✔ Admin Dashboard for reviewing ideas  
✔ Accept / Reject / Hold ideas  
✔ Idea status tracking (Pending, Approved, Rejected)  
✔ Responsive UI using Bootstrap  
✔ Secure & scalable Django backend  


## 🛠️ Tech Stack

**Frontend:**  
- HTML5, CSS3  
- Bootstrap  

**Backend:**  
- Python  
- Django Framework  

**Database:**  
- SQLite (default)  


## 📁 Project Structure

IDEALOGPROJECT/
│── users/ # User login/registration
|__ dashboard/ # Dashboard for users
│── Ideas/ # Main ideas files for creating ideas
|__ teams/ # Collaboration with other users
│── templates/ # HTML templates
│── static/ # CSS, Images
│── IdealogProject/ # Project configuration files
│── db.sqlite3 # Database (local)
│── manage.py



## ⚙️ Installation & Setup

Follow these steps to run the project locally:

### **1️⃣ Clone the repository**
git clone https://github.com/snehal-145/idealog-django-project.git
cd idealog-django-project


### **2️⃣ Create a virtual environment**
python -m venv env


### **3️⃣ Activate the environment**
**Windows:**
env\Scripts\activate


### **4️⃣ Install dependencies**
pip install -r requirements.txt


### **5️⃣ Apply migrations**
python manage.py migrate


### **6️⃣ Create superuser (for admin panel)**
python manage.py createsuperuser


### **7️⃣ Run the server**
python manage.py runserver



Your project will run at:  
👉 http://127.0.0.1:8000/




## 🧪 Usage Guide

1. Register or Login  
2. Submit your idea with title & description  
3. Admin can view all submitted ideas  
4. Admin approves, rejects, or keeps ideas pending  
5. Users can track idea status  


## 🚀 Future Improvements

- Add email notifications for idea updates  
- Add AI-based idea recommendation system  
- Add analytics dashboard for admin  
- Add REST API support  


## 👨‍💻 Author

**Snehal Wagavekar**  
GitHub: [snehal-145](https://github.com/snehal-145)

