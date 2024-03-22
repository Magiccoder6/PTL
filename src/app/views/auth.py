import functools

from flask import (
    Blueprint, flash, g, jsonify, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from app.db import get_db
from app.exceptions import InvalidAPIUsage

bp = Blueprint('auth', __name__, url_prefix='/')

@bp.route('/', methods=('GET', 'POST'))
def sign_in():    
    return render_template('sign_in.html')

@bp.route('/sign_up', methods=('GET', 'POST'))
def sign_up():    
    return render_template('sign_up.html')

@bp.route('/login', methods=('GET', 'POST'))
def submit_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(email)
        db = get_db()
        user = db.execute(
            'SELECT * FROM users WHERE email = ?', (email,)
        ).fetchone()

        if user is None:
            raise InvalidAPIUsage(message='Incorrect email.', status_code=400)
        elif not check_password_hash(user['pass'], password):
            raise InvalidAPIUsage(message='Incorrect password.', status_code=400)
        
        session.clear()
        session['user_id'] = user['id']
        return jsonify({'message': 'login success'})

@bp.route('/register', methods=('GET', 'POST'))
def submit_registration():
    if request.method == 'POST':
        email = request.form['email']
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        userRole = request.form['userRole']
        password = request.form['password']

        db = get_db()

        try:
            db.execute(
                "INSERT INTO users (email, firstName, lastName, userRole, pass) VALUES (?, ?, ?, ?, ?)",
                (email, firstName, lastName, userRole, generate_password_hash(password)),
            )
            db.commit()
        except db.IntegrityError:
            raise InvalidAPIUsage(message=f"User {email} is already registered.", status_code=400)
        except Exception as e:
            print(e)
            raise InvalidAPIUsage(message=e.__dict__, status_code=500)
        
    return jsonify({'message': 'success'})

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM users WHERE id = ?', (user_id,)
        ).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.sign_in'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.sign_in'))

        return view(**kwargs)

    return wrapped_view