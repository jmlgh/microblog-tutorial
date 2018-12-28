from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'javi'}
    posts = [
        {
            'author': {'username': 'javi'},
            'body': 'Open source is the future!'
        },
        {
            'author': {'username': 'ana'},
            'body': 'AstroBot is awesome!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # will return true when user clicks on submit and all fields are validated ok
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        # name of the view function
        return redirect(url_for('index'))
    return render_template('login.html', title="Sign In", form=form)