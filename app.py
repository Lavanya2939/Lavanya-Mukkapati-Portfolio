from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# ---------------- FIREBASE INIT ----------------
cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# ---------------- ROUTES -----------------------

@app.route('/')
def home():
    about_data = db.collection("about").document("main").get().to_dict()
    return render_template("index.html", about=about_data)

@app.route('/about')
def about():
    about_data = db.collection("about").document("main").get().to_dict()
    education_docs = db.collection("education").stream()
    education_data = [doc.to_dict() for doc in education_docs]
    return render_template("about.html", about=about_data, education=education_data)

@app.route('/skills')
def skills():
    skill_docs = db.collection("skills").stream()
    skills_data = [doc.to_dict() for doc in skill_docs]
    return render_template("skills.html", skills=skills_data)

@app.route('/projects')
def projects():
    project_docs = db.collection("projects").order_by("id", direction=firestore.Query.DESCENDING).stream()
    projects_data = [doc.to_dict() for doc in project_docs]
    return render_template("projects.html", projects=projects_data)

@app.route('/experience')
def experience():
    exp_docs = db.collection("experience").order_by("id", direction=firestore.Query.DESCENDING).stream()
    experience_data = [doc.to_dict() for doc in exp_docs]
    return render_template("experience.html", experience=experience_data)

@app.route('/contact')
def contact():
    return render_template("contact.html")

# ---------------- RUN SERVER -----------------------
if __name__ == '__main__':
    app.run(debug=True)
