from app import create_app, db
from app.auth.models import Kierowca


flask_app = create_app('dev')
with flask_app.app_context():
    db.create_all()
    if not Kierowca.query.filter_by(user_name='Łukasz').first():
        Kierowca.create_user(user='Łukasz',
                            city='Tychy',
                            password='TychyDzienKobiet')
flask_app.run()