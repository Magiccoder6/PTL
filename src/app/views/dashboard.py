import functools

from flask import (
    Blueprint, flash, g, jsonify, redirect, render_template, request, session, url_for
)

from app.db import get_db
from app.exceptions import InvalidAPIUsage

bp = Blueprint('index', __name__, url_prefix='/')

@bp.route('/dashboard', methods=('GET', 'POST'))
def dashboard():  

    return render_template('dashboard.html')