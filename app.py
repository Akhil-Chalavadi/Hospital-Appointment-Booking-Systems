
from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Development secret key. Change before production.
app.secret_key = "citycare-development-secret-key"


# Database connection
def get_db():
    conn = sqlite3.connect("hospital.db")
    conn.row_factory = sqlite3.Row
    return conn


# Create database
def create_database():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Patient registration
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        password = request.form["password"]

        hashed_password = generate_password_hash(password)

        conn = get_db()

        try:
            conn.execute("""
                INSERT INTO patients (name, email, phone, password)
                VALUES (?, ?, ?, ?)
            """, (name, email, phone, hashed_password))

            conn.commit()
            conn.close()

            return redirect(url_for("login"))

        except sqlite3.IntegrityError:
            conn.close()
            return render_template(
                "register.html",
                error="This email is already registered."
            )

    return render_template("register.html")


# Patient login
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        conn = get_db()
        patient = conn.execute(
            "SELECT * FROM patients WHERE email = ?",
            (email,)
        ).fetchone()
        conn.close()

        if patient and check_password_hash(
            patient["password"], password
        ):
            session["patient_id"] = patient["id"]
            return redirect(url_for("dashboard"))

        return render_template(
            "login.html",
            error="Invalid email or password."
        )

    return render_template("login.html")


# Patient dashboard
@app.route("/dashboard")
def dashboard():

    if "patient_id" not in session:
        return redirect(url_for("login"))

    conn = get_db()

    patient = conn.execute(
        "SELECT name, email, phone FROM patients WHERE id = ?",
        (session["patient_id"],)
    ).fetchone()

    conn.close()

    if patient is None:
        session.clear()
        return redirect(url_for("login"))

    return render_template("dashboard.html", patient=patient)


# Patient logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


if __name__ == "__main__":
    create_database()
    app.run(host="0.0.0.0", port=5000, debug=True)
