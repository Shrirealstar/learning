from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

db = SQLAlchemy(app)

from datetime import datetime

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    mobile = db.Column(db.String(15), nullable=False)
    designation = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    courses = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)


@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_user():
    username = request.form['username']
    password = request.form['password']
    if username == 'Admin' and password == 'Admin@123':
        return redirect(url_for('dashboard'))
    else:
        flash('Invalid credentials', 'danger')
        return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['mobile']
        designation = request.form['designation']
        gender = request.form['gender']
        courses = ','.join(request.form.getlist('course'))
        image = request.files['image']
        image_filename = ''

        if image:
            image_filename = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(image_filename)
            image_filename = image.filename

        new_employee = Employee(
            name=name,
            email=email,
            mobile=mobile,
            designation=designation,
            gender=gender,
            courses=courses,
            image=image_filename
        )
        db.session.add(new_employee)
        db.session.commit()

        flash('Employee added successfully', 'success')
        return redirect(url_for('employee_list'))

    return render_template('add_employee.html')

@app.route('/employee_list')
def employee_list():
    employees = Employee.query.all()
    return render_template('employee_list.html', employees=employees)

@app.route('/edit_employee/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
    employee = Employee.query.get_or_404(id)
    if request.method == 'POST':
        employee.name = request.form['name']
        employee.email = request.form['email']
        employee.mobile = request.form['mobile']
        employee.designation = request.form['designation']
        employee.gender = request.form['gender']
        employee.courses = ','.join(request.form.getlist('course'))

        image = request.files['image']
        if image:
            image_filename = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(image_filename)
            employee.image = image.filename

        db.session.commit()
        flash('Employee updated successfully', 'success')
        return redirect(url_for('employee_list'))

    return render_template('edit_employee.html', employee=employee)

@app.route('/delete_employee/<int:id>', methods=['POST'])
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    flash('Employee deleted successfully', 'success')
    return redirect(url_for('employee_list'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)