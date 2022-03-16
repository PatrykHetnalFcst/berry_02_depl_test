from click import confirm
from flask_wtf  import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError


class RegistrationForm(FlaskForm):
    name = StringField('Imię', validators=[DataRequired(), Length(2,15,message='nazwa musi zawierać pomiędzy 3 a 15 znaków')])
    city = StringField('Miasto',validators=[DataRequired()])
    password = PasswordField('Hasło',validators=[DataRequired(), Length(5), EqualTo('confirm', message='hasła muszą być takie same')])
    confirm = PasswordField('Potwierdź',validators=[DataRequired()])
    submit = SubmitField('Zarejestruj')

class LoginForm(FlaskForm):
    name = StringField('Imię', validators=[DataRequired()])
    password = PasswordField('Hasło',validators=[DataRequired()])
    stay_loggedin = BooleanField('Pozosatń zalogowanym')
    submit = SubmitField('Zaloguj')

    