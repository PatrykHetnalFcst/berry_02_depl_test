from app.raport import main
from app import db
from app.raport.forms import SendRaportForm
from app.raport.models import Sprzedaz, Stany_wyjsciowe, Stoiska
from app.auth.models import Kierowca
from flask import render_template, request, redirect, url_for, flash, session
from flask_login import current_user, login_required
from datetime import datetime




@main.route('/wyslij', methods=['GET','POST'])
@login_required
def wyslij():
    stany_wyjsciowe = Stany_wyjsciowe.query.all()
    today = datetime.today().strftime('%d-%m-%Y')
    miasto_kierowcy = Kierowca.query.filter_by(user_name=session['username']).first().user_city
    stoiska_kierowcy = Stoiska.query.filter_by(miasto=miasto_kierowcy).all()
    form = SendRaportForm(stoiska_kierowcy)
    if form.validate_on_submit():
        sprzedaz_r = Sprzedaz(miasto=miasto_kierowcy, kierowca=session['username'], stoisko=form.stoisko_k.data,data=today, godzina=form.godzina.data, towar='róże',sprzedane=form.sprzedane_roze.data)
        sprzedaz_t = Sprzedaz(miasto=miasto_kierowcy, kierowca=session['username'], stoisko=form.stoisko_k.data,data=today, godzina=form.godzina.data, towar='tulipany',sprzedane=form.sprzedane_tulipany.data)
        db.session.add_all([sprzedaz_r,sprzedaz_t])
        db.session.commit()
        return redirect(url_for("main.raport_wyslany"))

    return render_template('wyslij.html', form=form, stany_wyjsciowe=stany_wyjsciowe,miasto_kierowcy=miasto_kierowcy,stoiska_kierowcy=stoiska_kierowcy)

@main.route('/', methods=['GET','POST'])
def index():

    return render_template('index.html')

@main.route('/raport_wyslany')
def raport_wyslany():

    return render_template('raport_wyslany.html')