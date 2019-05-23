from flask import jsonify
from flask import render_template
from flask import url_for

from flanagan import app
from flanagan.forms import RegisterForm
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect(app)  # Register CSRF into app globally

app.config['SECRET_KEY'] = 'iDontEvenKnowWhatImDoing'  # Required for csrf
app.config['RECAPTCHA_USE_SSL'] = False
app.config['RECAPTCHA_PUBLIC_KEY'] = 'enter_your_public_key'
app.config['RECAPTCHA_PRIVATE_KEY'] = 'enter_your_private_key'
app.config['RECAPTCHA_OPTIONS'] = {'theme': 'black'}


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/template/')
@app.route('/template/<name>')
def template(name=None):
    return render_template('template.html', name=name)


@app.route('/hello', methods=['GET'])
def hello():
    return 'Hello, World, url = {}'.format(url_for('hello'))


@app.route('/form', methods=['GET', 'POST'])
def form():
    form = RegisterForm()

    if form.validate_on_submit():
        # TODO: Special things
        return jsonify(form.data)

    return render_template("form.html", form=form)
