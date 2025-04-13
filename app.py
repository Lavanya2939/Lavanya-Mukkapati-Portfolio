from flask import Flask, render_template
import pymysql

app = Flask(__name__)

# Database connection setup
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='portfolio_db',
    cursorclass=pymysql.cursors.DictCursor
)

# ---------------------- ROUTES -----------------------

@app.route('/')
def home():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM about WHERE id = 1")
        about_data = cursor.fetchone()
    return render_template("index.html", about=about_data)

@app.route('/about')
def about():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM about WHERE id = 1")
        about_data = cursor.fetchone()
        cursor.execute("SELECT * FROM education ORDER BY id ASC")
        education_data = cursor.fetchall()
    return render_template("about.html", about=about_data, education=education_data)


@app.route('/skills')
def skills():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM skills ORDER BY category, name")
        skills_data = cursor.fetchall()
    return render_template("skills.html", skills=skills_data)

@app.route('/projects')
def projects():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM projects ORDER BY id DESC")
        projects_data = cursor.fetchall()
    return render_template("projects.html", projects=projects_data)

@app.route('/experience')
def experience():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM experience ORDER BY id DESC")
        experience_data = cursor.fetchall()
    return render_template("experience.html", experience=experience_data)

@app.route('/contact')
def contact():
    return render_template("contact.html")

# ---------------------- RUN SERVER -----------------------

if __name__ == '__main__':
    app.run(debug=True)
