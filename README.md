# Flask URL Shortner
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Web_App-black)
![Deployment](https://img.shields.io/badge/Deployment-Railway-purple)

A modern Flask-based URL shortener web application that converts long URLs into short, shareable links with real-time click tracking and dashboard analytics.

## Live Demo

[Visit Live Website](https://shortify-url-shortner.up.railway.app/)

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
https://shortify-url-shortner.up.railway.app/s/8TCSnz
```

---

## Screenshots

### Home Page

<img width="1913" height="968" alt="{37F20E05-87C4-4240-9459-82DF55FD7995}" src="https://github.com/user-attachments/assets/50198dfb-36fb-4520-b6b9-9391746b2d8f" />

### Dashboard Page

<img width="1920" height="970" alt="{0490E3F2-97CB-4794-9A6B-8E38DB36BBE1}" src="https://github.com/user-attachments/assets/35b9deef-6725-4e85-85ef-6d00f34d81cc" />

---
## 🔌 API

Retrieve all stored links:
```
/api/links
```

Example response:

```json
{
  "2dYOCS": {
    "clicks": 0,
    "url": "https://www.dtu.ac.in"
  },
  "8TCSnz": {
    "clicks": 3,
    "url": "https://www.google.com"
  },
  "vHg2cg": {
    "clicks": 1,
    "url": "https://www.youtube.com"
  }
}
```

---

### Author

Bhavishay Goyal
