<div align="center">
  
![ALX-Banner](https://github.com/elyse502/alx-backend/assets/125453474/eb1e33ed-9628-43e7-b44d-034313502cf9)
</div>

<p align="center">
<h2 align="center"><img align="center" src="https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png" alt="footer" width="150"  height="150"/></h2>

<div align="center">
  
# ALX WEB-Stack Portfolio: `Note App🗒️`
</div>

Welcome to my ALX Final Portfolio! This portfolio showcases the development of a **Note App**, which is a web-based application developed as part of the ALX-Africa Software Engineering programme. Below, you'll find detailed information about the project, its components, and how to set it up.

## Table of Contents

- [Overview](#overview)
- [Technologies-Used](#technologies-used)
- [Components](#components)
- [Installation](#installation)
- [Usage](#usage)
- [Structure](#structure)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)
- [License](#license)

<div align="center">
  
![unnamed](https://github.com/elyse502/note-app/assets/125453474/66ba841a-efb0-41dc-ba4d-368906d2c9c2)
</div>

---

## Overview

The **Note App** is a web-based application designed to allow users to create, view, and delete notes. It's built using the Flask web framework and incorporates features such as user authentication, database storage, and dynamic rendering of content. The project demonstrates proficiency in backend development and serves as a showcase of Full Stack Software Engineering skills.

---

## Technologies-Used
The Note App project utilizes the following technologies and tools:

* **Flask:** A lightweight web application framework for Python.
* **Object-Oriented Programming (OOP)**: Utilized for efficient code organization and maintainability.
* **SQLite:** A relational database management system used for storing user data and notes.
* **Flask-Login:** A Flask extension for managing user sessions and authentication.
* **Bootstrap:** A front-end framework for designing responsive and mobile-first websites.
* **JavaScript:** Used for client-side scripting and dynamic interactions.
* **jQuery:** A fast, small, and feature-rich JavaScript library for simplifying client-side scripting.
* **HTML:** The standard markup language for creating web pages and applications.
* **CSS:** Cascading Style Sheets for styling HTML elements and enhancing the visual presentation.
* **Git:** A version control system for tracking changes in the project codebase.
* **GitHub:** A platform for hosting and collaborating on Git repositories.

These technologies collectively enable the development of a robust and user-friendly web application for managing notes effectively.

---

## Components

The project consists of the following components:

- `Src/` - The main directory containing the application source code.
  - `instance/` - Directory containing the SQLite database file (`database.db`).
  - `website/` - Directory containing the Flask application code.
    - `static/` - Directory containing static files such as CSS and JavaScript.
      - `index.js` - JavaScript file containing client-side functionality.
    - `templates/` - Directory containing HTML templates.
      - `base.html`, `home.html`, `login.html`, `sign_up.html` - HTML templates for different pages.
    - `__init__.py`, `auth.py`, `models.py`, `views.py` - Python modules containing application logic.
- `main.py` - Main Python script to run the Flask application.
- `requirements.txt` - File containing dependencies required to run the application.

---

## Installation

To install and run the Note App on your local machine, follow these steps:

1. Clone the repository:

   ```groovy
   $ git clone https://github.com/your-username/note-app.git
   ```

2. Navigate to the project directory:

   ```groovy
   $ cd note-app
   ```

3. Create a virtual environment (optional but recommended):

   ```groovy
   $ python -m venv venv
   ```

4. Activate the virtual environment:
    * On Windows:

   ```groovy
   $ venv\Scripts\activate
   ```
   * On macOS and Linux:

   ```groovy
   $ source venv/bin/activate
   ```

5. Install dependencies:

   ```groovy
   $ pip install -r requirements.txt
   ```

6. Run the Flask application:

   ```groovy
   $ python main.py
   ```
7. Access the application in your web browser at `http://localhost:5000`.

---

## Usage
Once the application is running, you can access it in your web browser. Here are some key features:

* **Home Page**: View existing notes and add new ones.
* **Login Page**: Authenticate with your email and password.
* **Sign-Up Page**: Create a new account.
* **Logout**: Log out of the application.

---

## Structure
Here is the `Structure` of the **note-app🗒️**:
```groovy
elysee_niyibizi@HACKER:~/note-app$ ls
AUTHORS  LICENSE  README.md  Src  requirements.txt  venv
elysee_niyibizi@HACKER:~/note-app$ tree -I venv
.
├── AUTHORS
├── LICENSE
├── README.md
├── Src
│   ├── instance
│   │   └── database.db
│   ├── main.py
│   └── website
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-312.pyc
│       │   ├── __init__.cpython-38.pyc
│       │   ├── auth.cpython-312.pyc
│       │   ├── auth.cpython-38.pyc
│       │   ├── models.cpython-312.pyc
│       │   ├── models.cpython-38.pyc
│       │   ├── views.cpython-312.pyc
│       │   └── views.cpython-38.pyc
│       ├── auth.py
│       ├── models.py
│       ├── static
│       │   └── index.js
│       ├── templates
│       │   ├── base.html
│       │   ├── home.html
│       │   ├── login.html
│       │   └── sign_up.html
│       └── views.py
└── requirements.txt

6 directories, 23 files
elysee_niyibizi@HACKER:~/note-app$
```

---

## Contributing
Contributions to the Note App project are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/new-feature`).
6. Create a new Pull Request.

---

## Acknowledgements
I would like to express my gratitude to the following individuals and organizations for their support and guidance throughout my journey in the [ALX-Africa](https://tech.alxafrica.com/rwanda?utm_source=google&utm_medium=pmax&utm_campaign=kgl_2024q1&utm_term=tofu-applications-tech-lite-rw&gad_source=1&gclid=CjwKCAiA_5WvBhBAEiwAZtCU70OGXSQKneP9Knvb8LXGqW0FOhcSbUJvZds7kCS2QXKmNYhQGVUHMxoCq3cQAvD_BwE) Software Engineering programme:

* My **Mentors** for their valuable feedback and assistance.
* My peers in **`Cohort 13`** for their collaboration and camaraderie.
* [**ALX Africa:**](https://www.alxafrica.com/) Thank you for providing a transformative software engineering program that has equipped me with the skills and knowledge needed to pursue a career in technology. Your commitment to fostering talent and promoting lifelong learning is truly commendable.
* [**Mastercard Foundation:**](https://mastercardfdn.org/) I am immensely grateful for the opportunity to participate in the ALX Africa program, made possible through your generous sponsorship. Your commitment to empowering African youth with the technical skills and resources necessary to thrive in the global workforce is truly inspiring.
* [**Fred Swaniker:**](https://en.wikipedia.org/wiki/Fred_Swaniker) I extend my sincere appreciation to Fred Swaniker for his visionary leadership and dedication to creating the next generation of African leaders and innovators. His unwavering belief in the potential of African talent has been instrumental in driving positive change and progress across the continent.

<div align="center">

_**A good `note-taking` system is essential for capturing information [@kalibetre](https://twitter.com/kalibetre/status/1770038721267618025)✍️**. For more info visit 👉 [LINK](https://www.google.com/search?q=A+good+note-taking+system+is+essential+for+capturing+information&oq=A+good+note-taking+system+is+essential+for+capturing+information&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRhAMgYIAhBFGEAyBggDEEUYPTIGCAQQRRg80gEHNTkxajBqN6gCALACAA&sourceid=chrome&ie=UTF-8) ........😉_
</div>

---

## Author :black_nib:
1. _[NIYIBIZI Elysée](https://linktr.ee/niyibizi_elysee)👨🏿‍💻 | [Github](https://github.com/elyse502) | [Linkedin](https://www.linkedin.com/in/niyibizi-elys%C3%A9e/) | [Twitter](https://twitter.com/Niyibizi_Elyse)._

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**_Thank you for visiting my ALX Final Portfolio! If you have any questions or feedback, feel free to reach out. Regards🙏_**
</div>

---

## Support🎉
If you like how I present and document my work do me a favor of giving a Star ✨ to my [Repos](https://github.com/elyse502?tab=repositories) |&&| a [Follow](https://github.com/elyse502) 👥

<p align="center">
<h2 align="center"><img align="center" src="https://github.com/elyse502/AirBnB_clone/assets/125453474/ab3c1e01-2b98-47ae-96b7-37c07c85a2f1" alt="footer" width="150"  height="150"/></h2>





