from flask import Flask,render_template,request,session,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,login_manager,LoginManager
from flask_login import login_required,current_user
from flask_mail import Mail
import json

# MY db connection
local_server= True
app = Flask(__name__)
app.secret_key='ashwinsivak'

# get unique user access
login_manager=LoginManager(app)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# app.config['SQLALCHEMY_DATABASE_URL']='mysql://username:password@localhost/database_table_name'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/fms'
db=SQLAlchemy(app)

# create db tables
class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    email=db.Column(db.String(100))

class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50))
    email=db.Column(db.String(50),unique=True)
    password=db.Column(db.String(1000))    

# pass endpoints and functions
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flights')
def flights():
    if not User.is_authenticated:
        return render_template('login.html')
    else:
        return render_template('flights.html',username=current_user.username)
    return render_template('flights.html')

@app.route('/arrivals')
def arrivals():
    return render_template('arrivals.html')

@app.route('/departures')
def departures():
    return render_template('departures.html')
   

@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method == "POST":
       username=request.form.get('username')
       email=request.form.get('email')
       password=request.form.get('password')
       user=User.query.filter_by(email=email).first()
       if user:
            flash("Email Already Exist","warning")
            return render_template('signup.html')
       encpassword=generate_password_hash(password)
       # insert to db 
       new_user=db.engine.execute(f"INSERT INTO `user` (`username`,`email`,`password`) VALUES ('{username}','{email}','{encpassword}')")
       flash("Signup Succes Please Login","success")
       return render_template('login.html')
    return render_template('signup.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == "POST":
        email=request.form.get('email')
        password=request.form.get('password')
        user=User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password,password):
            login_user(user)
            flash("Login Success","primary")
            return redirect(url_for('flights'))
        else:
            flash("invalid credentials","danger")
            return render_template('login.html')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
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
