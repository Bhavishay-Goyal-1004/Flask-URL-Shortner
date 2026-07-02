from flask import Flask, render_template, request, redirect, jsonify
import json
import os
import random
import string

app = Flask(__name__)

DATA_FILE = "data.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as file:
        json.dump({}, file)


# LOAD DATA FROM JSON
def load_data():
    with open(DATA_FILE, "r") as file:
        return json.load(file)


# SAVE DATA TO JSON
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# GENERATE UNIQUE SHORT CODE
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits

    while True:
        short_code = ''.join(
            random.choice(characters)
            for i in range(length)
        )

        data = load_data()

        if short_code not in data:
            return short_code


@app.route('/')
def home():
    return render_template(
        "index.html",
        error=None,
        short_url=None
    )


@app.route('/shorten', methods=['POST'])
def shorten_url():

    original_url = request.form.get("url")


    if not original_url or original_url.strip() == "":
        return render_template(
            "index.html",
            error="Please enter a URL.",
            short_url=None
        )

    if not original_url.startswith(("http://", "https://")):
        return render_template(
            "index.html",
            error="URL must start with http:// or https://",
            short_url=None
        )


    data = load_data()

    short_code = generate_short_code()


    data[short_code] = {
        "url": original_url,
        "clicks": 0
    }

    save_data(data)

    short_url = request.host_url + "s/" + short_code

    return render_template(
        "index.html",
        error=None,
        short_url=short_url
    )



@app.route('/s/<code>')
def redirect_to_original(code):

    data = load_data()

    if code not in data:
        return render_template(
            "404.html",
            code=code
        ), 404


    data[code]["clicks"] += 1

    save_data(data)

    original_url = data[code]["url"]

    return redirect(original_url)


# DASHBOAR ~ Show all shortened URLs


@app.route('/dashboard')
def dashboard():

    data = load_data()

    return render_template(
        "dashboard.html",
        links=data
    )

# Return all links as JSON
@app.route('/api/links')
def api_links():

    data = load_data()

    return jsonify(data)


if __name__ == "__main__":

    app.run( host="0.0.0.0", port=5000)