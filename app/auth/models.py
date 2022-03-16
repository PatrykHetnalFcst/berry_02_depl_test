from app import db, bcrypt
from datetime import datetime
from flask_login import UserMixin
from app import login_manager

class Kierowca(UserMixin, db.Model):
    __tablename__ = 'kierowcy'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20))
    user_city = db.Column(db.String(20))
    user_password = db.Column(db.String(80))
    registration_date = db.Column(db.DateTime, default=datetime.now)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.user_password, password)

    @classmethod
    def create_user(cls, user, city, password):
        user=cls(
            user_name=user,
            user_city=city,
            user_password=bcrypt.generate_password_hash(password).decode('utf-8')
        )

        db.session.add(user)
        db.session.commit()

        return user

@login_manager.user_loader
def load_user(id):
    return Kierowca.query.get(int(id))