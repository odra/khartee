from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def root() -> str:
    """
    Root flask handler, will render the root.html template.
    """
    return render_template('root.html')


@app.route('/signin')
def signin() -> str:
    """
    Root flask handler, will render the root.html template.
    """
    return render_template('login.html')


@app.route('/signup')
def signup() -> str:
    """
    Root flask handler, will render the root.html template.
    """
    return render_template('signup.html')


def run() -> None:
    """
    Runs flask app in dev mode, should not be in production.

    Application will be exposed to port 5000.
    """
    app.run()
