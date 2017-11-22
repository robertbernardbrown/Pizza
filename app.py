from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
app.secret_key = "my precious"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

#defining the login manager class for flask_login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

#create a DB to hold users' credentials
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

#retrieves user information if the login information matches
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#create a login form that must fit certain parameters
class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=20)])
    remember = BooleanField('remember me')

#create a registration form that must fit certain parameters
class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid Email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=20)])

#def login_required(f):
#    @wraps(f)
#    def wrap(*args, **kwargs):
#        if 'logged_in' in session:
#            return f(*args, **kwargs)
#        else:
#            flash('You need to login first.')
#            return redirect(url_for('login'))
#    return wrap

#login route. Will prompt for login username or password. If credentials do not exist will return flsah message, otherwise will login
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm()
    if form.is_submitted():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect ('order')

        else:
            error = 'Invalid username or password'
    return render_template('login.html', form=form, error=error)

#base home route. Where the user is directed after login
@app.route('/')
def home():
    return render_template('base.html')


@app.route('/input')
@login_required
def input():
		return render_template('input.html')

@app.route('/order')
@login_required
def order():
		return render_template('order.html')

@app.route('/finally')
@login_required
def final():
		return render_template('finally.html')

#signup route. Where the user is sent to register a username and password
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.is_submitted():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('New User has been created')
        return redirect ('login')

    return render_template('signup.html', form=form)

#logout route. Logs a user out when they press the button to visit this page
@app.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You were just logged out')
	return redirect(url_for('home'))

if __name__ == '__main__':
		app.run(debug=True)
