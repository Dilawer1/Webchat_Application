import MySQLdb
from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)

# MySQL configuration
db =MySQLdb.connect(
    host='127.0.0.1',
    user='webchatuser',
    password='root',
    database='webchatdb',
    cursorclass=pymysql.cursors.DictCursor
)

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['Full Name']
        email = request.form['Email']
        phone = request.form['Phone']
        password = request.form['password']
        confirm_password = request.form['Confirm_password']
        dob = request.form['Date of Birth']
        mobile = request.form[ 'Mobile Number']

        # Check if the email already exists in the database
        with db.cursor() as cursor:
            sql = "SELECT * FROM users WHERE email = %s"
            cursor.execute(sql, (email,))
            user = cursor.fetchone()

            if user:
                error = "Email already exists. Please use a different email."
                return render_template('register.html', error=error)
            
            # Insert the user data into the database
            sql = "INSERT INTO users (name, email, phone, password, dob) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (name, email, phone, password, dob))
            db.commit()

        return redirect('/login')
    else:
        return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check if the email and password match a user in the database
        with db.cursor() as cursor:
            sql = "SELECT * FROM users WHERE email = %s AND password = %s"
            cursor.execute(sql, (email, password))
            user = cursor.fetchone()

            if user:
                # User login successful
                return redirect('/dashboard')
            else:
                error = "Invalid email or password. Please try again."
                return render_template('login.html', error=error)
    else:
        return render_template('login.html ./templates')

@app.route('/dashboard')
def dashboard():
    # Check if the user is logged in
    # If not, redirect to the login page
    # You can use session or cookies to manage user authentication
    
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run()
