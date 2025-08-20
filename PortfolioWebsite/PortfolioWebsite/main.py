
from flask import Flask, render_template, request, redirect, url_for, flash
from collections import defaultdict
import datetime

app = Flask(__name__)
app.secret_key = "your-secret-key"

# In-memory analytics (can later be replaced with DB)
analytics = {
    "page_views": defaultdict(int),
    "form_submissions": []
}

# Simple dashboard password (change to something secure)
DASHBOARD_PASSWORD = "MySecurePass123"

# Track page views
def track_page(page_name):
    analytics["page_views"][page_name] += 1

@app.route("/")
def home():
    track_page("Home")
    return render_template("index.html")

@app.route("/about")
def about():
    track_page("About")
    return render_template("about.html")

@app.route("/projects")
def projects():
    track_page("Projects")
    return render_template("projects.html")

@app.route("/services")
def services():
    track_page("Services")
    skills = [
        {"name": "Python", "percent": 90, "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"},
        {"name": "JavaScript", "percent": 85, "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg"},
        {"name": "HTML & CSS", "percent": 95, "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg"},
        {"name": "Flask", "percent": 80, "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg"},
        {"name": "Tailwind CSS", "percent": 85, "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tailwindcss/tailwindcss-plain.svg"},
    ]
    return render_template("services.html", skills=skills)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    track_page("Contact")
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        analytics["form_submissions"].append({
            "name": name,
            "email": email,
            "message": message,
            "timestamp": datetime.datetime.now()
        })
        flash("Message sent successfully!", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html")


@app.route("/dashboard-login", methods=["GET", "POST"])
def dashboard_login():
    if request.method == "POST":
        password = request.form.get("password")
        if password == DASHBOARD_PASSWORD:
            session["dashboard_logged_in"] = True
            return redirect(url_for("dashboard"))
        else:
            flash("Incorrect password", "error")
            return redirect(url_for("dashboard_login"))
    return render_template("dashboard_login.html")

@app.route("/dashboard")
def dashboard():
    if not session.get("dashboard_logged_in"):
        return redirect(url_for("dashboard_login"))

    submissions = sorted(analytics["form_submissions"], key=lambda x: x["timestamp"], reverse=True)
    return render_template("dashboard.html", analytics=analytics, submissions=submissions)

@app.route("/dashboard-logout")
def dashboard_logout():
    session.pop("dashboard_logged_in", None)
    flash("Logged out successfully", "success")
    return redirect(url_for("dashboard_login"))




