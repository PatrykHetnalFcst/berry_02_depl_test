
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, RadioField
from wtforms.validators import DataRequired

class SendRaportForm(FlaskForm):
    def __init__(self, stoiska_kierowcy):
        super().__init__()
        self.stoisko_k.choices = [(x.stoisko, x.stoisko) for x in stoiska_kierowcy]

    godzina = RadioField('Godzina', choices=['12','14','16'])
    
    stoisko_k = RadioField('Stoisko')
    sprzedane_roze = IntegerField('Sprzedane róże: ',validators=[DataRequired()])
    sprzedane_tulipany = IntegerField('Sprzedane tulipany: ',validators=[DataRequired()])
    submit = SubmitField('Wyślij')