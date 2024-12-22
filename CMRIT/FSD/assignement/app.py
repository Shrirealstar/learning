from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_session import Session
from datetime import datetime
import sqlite3
import os
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Database setup
DATABASE = 'employees.db'
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            mobile TEXT NOT NULL,
            designation TEXT NOT NULL,
            gender TEXT NOT NULL,
            courses TEXT NOT NULL,
            image TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

USERNAME = "Admin"
PASSWORD = "Admin@123"

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == USERNAME and password == PASSWORD:
        session['user'] = "Shrishaila .P"
        return redirect(url_for('dashboard'))
    else:
        return render_template('login.html', error="Invalid username or password!")

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html', name=session['user'])
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if 'user' not in session:
        return redirect(url_for('home'))

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['mobile']
        designation = request.form['designation']
        gender = request.form['gender']
        courses = request.form.getlist('course')
        image = request.files['image']
        
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])

        # Validate email
        if not re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', email):
            flash('Invalid email address!', 'error')
            return redirect(url_for('add_employee'))

        # Validate image
        if image.filename == '' or not image.filename.lower().endswith(('.jpg', '.png')):
            flash('Please upload a valid image file (JPG or PNG)', 'error')
            return redirect(url_for('add_employee'))

        filename = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(filename)

        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO employees (name, email, mobile, designation, gender, courses, image, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, email, mobile, designation, gender, ', '.join(courses), filename, created_at))
        conn.commit()
        conn.close()

        flash('Employee added successfully!', 'success')
        return redirect(url_for('employee_list'))

    return render_template('add_employee.html')

@app.route('/employee_list')
def employee_list():
    if 'user' not in session:
        return redirect(url_for('home'))

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    conn.close()

    return render_template('employee_list.html', employees=employees)

@app.route('/edit_employee/<int:employee_id>', methods=['GET', 'POST'])
def edit_employee(employee_id):
    if 'user' not in session:
        return redirect(url_for('home'))

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['mobile']
        designation = request.form['designation']
        gender = request.form['gender']
        courses = request.form.getlist('course')
        image = request.files['image']
        updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if image.filename:
            if not image.filename.lower().endswith(('.jpg', '.png')):
                flash('Please upload a valid image file (JPG or PNG)', 'error')
                return redirect(url_for('edit_employee', employee_id=employee_id))

            filename = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(filename)
        else:
            cursor.execute('SELECT image FROM employees WHERE id = ?', (employee_id,))
            filename = cursor.fetchone()[0]

        cursor.execute('''
            UPDATE employees SET name = ?, email = ?, mobile = ?, designation = ?, gender = ?, courses = ?, image = ?, updated_at = ? WHERE id = ?
        ''', (name, email, mobile, designation, gender, ', '.join(courses), filename, updated_at, employee_id))
        conn.commit()
        conn.close()

        flash('Employee updated successfully!', 'success')
        return redirect(url_for('employee_list'))

    cursor.execute('SELECT * FROM employees WHERE id = ?', (employee_id,))
    employee = cursor.fetchone()
    conn.close()

    return render_template('edit_employee.html', employee=employee)

@app.route('/delete_employee/<int:employee_id>', methods=['POST'])
def delete_employee(employee_id):
    if 'user' not in session:
        return redirect(url_for('home'))

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM employees WHERE id = ?', (employee_id,))
    conn.commit()
    conn.close()

    flash('Employee deleted successfully!', 'success')
    return redirect(url_for('employee_list'))

if __name__ == '__main__':
    app.run(debug=True)
