from app import create_app, db
from app.auth.models import Kierowca

if __name__ == '__main__': ## Tabs changed
    flask_app = create_app('prod')
    with flask_app.app_context():
        db.create_all()
        if not Kierowca.query.filter_by(user_name='Łukasz').first():
            Kierowca.create_user(user='Łukasz',
                                city='Tychy',
                                password='TychyDzienKobiet')
    flask_app.run()