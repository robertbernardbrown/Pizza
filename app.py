from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps

app = Flask(__name__)

app.secret_key = "my precious"

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'invalid credentials. Please try again.'
		else:
			session['logged_in'] = True
			flash('you were just logged in')
			return redirect(url_for('login'))
	return render_template('login.html', error=error)

@app.route('/')
def home():
		return render_template('base.html')

@app.route('/input')
@login_required
def input():
		return render_template('input.html')

@app.route('/choice')
@login_required
def choice():
		return render_template('choice.html')

@app.route('/finally')
@login_required
def final():
		return render_template('finally.html')

@app.route('/signup')
def signup():
		return render_template('signup.html')

@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in', None)
	flash('You were just logged out')
	return redirect(url_for('login'))

if __name__ == '__main__':
		app.run(debug=True)
        
