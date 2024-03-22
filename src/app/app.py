from flask import jsonify
from app import create_app
from app.exceptions import InvalidAPIUsage

app = create_app()

@app.route('/')
def login_register():

    return 'Register or login now'

@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(e):
    return jsonify(e.to_dict()), e.status_code