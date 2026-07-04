# Flask URL Shortner
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Web_App-black)
![Deployment](https://img.shields.io/badge/Deployment-Railway-purple)

A modern Flask-based URL shortener web application that converts long URLs into short, shareable links with real-time click tracking and dashboard analytics.

## Live Demo

[Visit Live Website](https://flask-url-shortner-production.up.railway.app/)

---

## Features

- Shorten long URLs instantly
- Generate unique short links
- Fast redirection system
- Click tracking support
- Responsive modern UI
- Dashboard to manage links
- REST API endpoint
- URL validation handling
- JSON-based lightweight storage
- Railway cloud deployment

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
git clone https://github.com/Bhavishay-Goyal-1004/Flask-URL-Shortner.git
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
https://flask-url-shortner-production.up.railway.app/s/YVapoV
```

---

## Screenshots

### Home Page

<img width="1918" height="1031" alt="{6F93C71A-A68A-4D2B-8FA5-B52BA8C25426}" src="https://github.com/user-attachments/assets/724022e2-58cc-436b-87a0-9bea066cefa7" />

### Dashboard Page

<img width="1920" height="1031" alt="{2F8D8EB5-3640-4FC7-99C7-2774CCCABEC9}" src="https://github.com/user-attachments/assets/e6cd8f44-fd32-49d0-a067-792860bd1b05" />

---
## 🔌 API

Retrieve all stored links:
```
/api/links
```

Example response:

```json
{
  "Na6UTf": {
    "clicks": 1,
    "url": "https://www.youtube.com"
  },
  "YVapoV": {
    "clicks": 0,
    "url": "https://www.google.com"
  }
}
```

---

### Author

Bhavishay Goyal
