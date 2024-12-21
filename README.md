SecureWebApp
SecureWebApp is an open-source educational web application designed to demonstrate secure and insecure coding practices. It is a simple blog platform where users can register, log in, and create posts. The application has two versions:

A secure version, showcasing proper security implementations.
An insecure version, deliberately introducing vulnerabilities for educational purposes.
Features
User Registration:

Secure: Passwords are hashed using werkzeug.security.
Insecure: Passwords are stored in plaintext.
User Authentication:

Secure: Prevents SQL injection using parameterized queries.
Insecure: Vulnerable to SQL injection attacks.
Post Management:

Users can create, view, and manage posts.
Secure: Protects against XSS attacks with output encoding.
Insecure: Vulnerable to XSS through user-generated content.
Security Demonstration:

Highlights vulnerabilities such as:
SQL Injection
XSS (Cross-Site Scripting)
Plaintext password storage
Security Mitigations (in the secure version):

Parameterized SQL queries.
Secure password hashing.
Implementation of security headers.
CSRF protection.
Technologies Used
Backend: Flask (Python)
Frontend: HTML/CSS
Database: SQLite3
Testing Tools:
OWASP ZAP for vulnerability scans.
Selenium for automated UI tests.
Setup Instructions
Clone the repository:

bash
Copy code
git clone https://github.com/Mkwenje/SecureWebApp.git
cd SecureWebApp
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
python app.py
Open your browser and navigate to http://127.0.0.1:5000.

Branch Details
Main Branch: Contains the secure version of the application with proper mitigations for vulnerabilities.
Secure Branch: Specifically focuses on demonstrating secure coding practices.
Insecure Branch: Deliberately introduces vulnerabilities for educational purposes.
Testing
Manual Testing
SQL Injection: In the insecure branch, use ' OR '1'='1 as input in the login form.
XSS: Add <script>alert('XSS')</script> in post content.
Automated Testing
Use OWASP ZAP to scan for vulnerabilities.
Use Selenium to automate functional testing.
Educational Purpose
This application is intended for educational use only. It demonstrates how vulnerabilities arise and how they can be mitigated using proper secure coding practices.

Contributing
We welcome contributions to improve this project! Please:

Fork the repository.
Create a new branch:
bash
Copy code
git checkout -b feature-name
Commit your changes and push:
bash
Copy code
git add .
git commit -m "Add feature-name"
git push origin feature-name
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
For questions or suggestions, feel free to reach out:

GitHub: Mkwenje
