from app import create_app

app = create_app()

@app.route('/')
def login_register():

    return 'Register or login now'