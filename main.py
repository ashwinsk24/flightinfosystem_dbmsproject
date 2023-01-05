from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_manager, LoginManager
from flask_login import login_required, current_user
from flask_mail import Mail
import json

# MY db connection
local_server = True
app = Flask(__name__)
app.secret_key = 'ashwinsivak'

# get unique user access
login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# app.config['SQLALCHEMY_DATABASE_URL']='mysql://username:password@localhost/database_table_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/fms'
db = SQLAlchemy(app)

# create db tables

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(1000))


class Flights(db.Model):
    email = db.Column(db.String(50))
    fid = db.Column(db.Integer, primary_key=True)
    flightno = db.Column(db.String(50))
    airline = db.Column(db.String(50))
    origin = db.Column(db.String(50),default='Cochin')
    destination = db.Column(db.String(50))
    date = db.Column(db.String(50), nullable=False)
    schd = db.Column(db.String(50), nullable=False)
    time = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50))
    terminal = db.Column(db.String(50))

# pass endpoints and functions

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/flights', methods=['POST', 'GET'])
@login_required
def flights():
    if request.method == "POST":
        email = request.form.get('email')
        flightno = request.form.get('flightno')
        airline = request.form.get('airline')
        origin = request.form.get('origin')
        destination = request.form.get('destination')
        date = request.form.get('date')
        schd = request.form.get('schd')
        time = request.form.get('time')
        status = request.form.get('status')
        terminal = request.form.get('terminal')
        subject = "Flight Info System"
        query = db.engine.execute(
            f"INSERT INTO `flights` (`email`,`flightno`,`airline`,`origin`,`destination`,`date`,`schd`,`time`,`status`,`terminal`) VALUES ('{email}','{flightno}','{airline}','{origin}','{destination}','{date}','{schd}','{time}','{status}','{terminal}')")
        flash("Flight data added", "info")
    return render_template('flights.html')


@app.route('/update')
@login_required
def update():
    em = current_user.email
    query = db.engine.execute(f"SELECT * FROM `flights` WHERE email='{em}'")
    return render_template('update.html', query=query)


@app.route('/departures')
def departures():
    query = db.engine.execute(
        f"SELECT `fid`,`flightno`, `airline`,`destination`, `date`, `schd`, `time`, `status`, `terminal` FROM `flights` WHERE origin='Cochin'")
    return render_template('departures.html', query=query)


@app.route('/arrivals')
def arrivals():
    query = db.engine.execute(
        f"SELECT `fid`,`flightno`, `airline`,`origin`, `date`, `schd`, `time`, `status`, `terminal` FROM `flights` WHERE destination='Cochin'")
    return render_template('arrivals.html', query=query)


@app.route("/edit/<string:fid>", methods=['POST', 'GET'])
@login_required
def edit(fid):
    posts = Flights.query.filter_by(fid=fid).first()
    if request.method == "POST":
        flightno = request.form.get('flightno')
        airline = request.form.get('airline')
        origin = request.form.get('origin')
        destination = request.form.get('destination')
        date = request.form.get('date')
        schd = request.form.get('schd')
        time = request.form.get('time')
        status = request.form.get('status')
        terminal = request.form.get('terminal')
        db.engine.execute(
            f"UPDATE `flights` SET `flightno` = '{flightno}', `airline` = '{airline}', `origin` = '{origin}', `destination` = '{destination}', `date` = '{date}', `schd` = '{schd}', `time` = '{time}', `status` = '{status}', `terminal` = '{terminal}' WHERE `flights`.`fid` = {fid}")
        flash("Flight data Updated", "success")
        return redirect('/update')

    return render_template('edit.html', posts=posts)


@app.route("/delete/<string:fid>", methods=['POST', 'GET'])
@login_required
def delete(fid):
    db.engine.execute(f"DELETE FROM `flights` WHERE `flights`.`fid`={fid}")
    flash("Flight data Deleted", "danger")
    return redirect('/flights')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email Already Exist", "warning")
            return render_template('signup.html')
        encpassword = generate_password_hash(password)
        # insert to db
        new_user = db.engine.execute(
            f"INSERT INTO `user` (`username`,`email`,`password`) VALUES ('{username}','{email}','{encpassword}')")
        flash("Signup Succes Please Login", "success")
        return render_template('login.html')
    return render_template('signup.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash("Login Success!", "primary")
            return redirect(url_for('index'))
        else:
            flash("Invalid credentials", "danger")
            return render_template('login.html')
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout Successfull", "warning")
    return redirect(url_for('login'))


@app.route('/test')
def test():
    try:
        Test.query.all()
        return 'connected'
    except:
        return 'not connected'
    return render_template('test.html')


app.run(debug=True)
