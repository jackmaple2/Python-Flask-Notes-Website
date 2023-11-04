from flask import Blueprint, render_template, request, flash
from flask_login import current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', boolean=True, user=current_user)

@auth.route('/logout')
def logout():
    return '<p>logout</p>'

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName= request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email entered is too short, must be more than three characters', category='error')
        elif len(firstName) < 2:
            flash('First name entered is too short, must be more than one character', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password entered is too short, must be more than seven characters', category='error')
        else:
            #add user to database
            flash('Account created!', category='success')
    return render_template('signup.html', user=current_user)