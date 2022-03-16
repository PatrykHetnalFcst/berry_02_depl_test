from flask import render_template, request, flash, redirect, url_for, session
from flask_login import login_required, login_user, logout_user, current_user
from app.auth.forms import RegistrationForm, LoginForm
from app.auth import authentication as at
from app.auth.models import Kierowca

@at.route('/register', methods=['GET', 'POST'])
def register_user():
    if current_user.is_authenticated:
        flash('Jesteś zalogowany')
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        Kierowca.create_user(
            user=form.name.data,
            city=form.city.data,
            password=form.password.data)
        flash('Zarejestrowano pomyślnie')
        return redirect(url_for('authentication.do_the_login'))

    return render_template('registration.html', form=form)

@at.route('/login', methods=['GET','POST'])
def do_the_login():
    if current_user.is_authenticated:
        flash('Jesteś zalogowany')
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Kierowca.query.filter_by(user_name=form.name.data).first()
        session['username']=form.name.data
        if not user or not user.check_password(form.password.data):
            flash('Błędny login lub hasło')
            return redirect(url_for('authentication.do_the_login'))
        
        login_user(user, form.stay_loggedin.data)
        return redirect(url_for('main.index'))

    return render_template('login.html', form=form)

@at.route('/logout')
@login_required
def log_out_user():
    logout_user()
    return redirect(url_for('main.index'))
