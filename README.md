# Flask URL Shortner

A fast and lightweight URL shortening web application built using Flask.
This project allows users to convert long URLs into short and shareable links with seamless redirection.

## Live Demo

[Visit Live Website](https://flask-url-shortner-production.up.railway.app/)

---

## Features

* Shorten long URLs instantly
* Fast URL redirection
* Clean and responsive user interface
* Lightweight Flask backend
* JSON-based data storage
* Railway deployment support
* Simple and beginner-friendly project structure

---

## Tech Stack

* Python
* Flask
* HTML5
* CSS3
* Gunicorn
* Railway
* JSON Storage

---

## Project Structure

```text
Flask-URL-Shortner/
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   └── 404.html
│
├── app.py
├── data.json
├── Procfile
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Flask-URL-Shortner.git
cd Flask-URL-Shortner
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open in your browser:

```text
http://127.0.0.1:5000
```

---

## Deployment

This application is deployed on Railway using Gunicorn.

### Procfile

```text
web: gunicorn app:app
```

---

## How It Works

1. User enters a long URL
2. Flask application generates a unique short code
3. URL mapping gets stored in `data.json`
4. Visiting the short URL redirects to the original website

---

## Example

### Original URL

```text
https://www.google.com
```

### Shortened URL

```text
http://flask-url-shortner-production.up.railway.app/s/TfJ8zF
```

---

## Screenshots

### Home Page

<img width="1920" height="910" alt="{68330A9D-1719-4F78-ABF7-F23D0B09B975}" src="https://github.com/user-attachments/assets/3aa015d1-3307-4f2e-a829-2d2f58ddf672" />

### Dashboard Page

<img width="1920" height="911" alt="{FF93AE2B-E2B6-4F95-A68B-85E3EA2906EE}" src="https://github.com/user-attachments/assets/abc5d97e-677d-44f2-a919-d89d3335b06c" />

---

### Author

Bhavishay Goyal
