from app import db

class Sprzedaz(db.Model):
    __tablename__ = 'sprzedaz'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    miasto = db.Column(db.String(99), nullable=False)
    kierowca = db.Column(db.String(99), nullable=False)
    stoisko = db.Column(db.String(99), nullable=False)
    data = db.Column(db.Date, nullable=False)
    godzina = db.Column(db.String(99), nullable=False)
    towar = db.Column(db.String(99), nullable=False)
    sprzedane = db.Column(db.Integer, nullable=False)

    def __init__(self, miasto, kierowca, stoisko, data, godzina, towar, sprzedane):
    
        self.miasto = miasto 
        self.kierowca = kierowca
        self.stoisko = stoisko
        self.data = data
        self.godzina = godzina
        self.towar = towar
        self.sprzedane = sprzedane 

class Stany_wyjsciowe(db.Model):
    __tablename__ = 'stany_wyjsciowe'

    id_stoiska = db.Column(db.Integer, primary_key=True)
    miasto = db.Column(db.String(99), nullable=False)
    stoisko = db.Column(db.String(99), nullable=False)
    data = db.Column(db.Date, nullable=False)
    towar = db.Column(db.String(99), nullable=False)
    stan_wyjsciowy = db.Column(db.Integer, nullable=False)

    def __init__(self, miasto, stoisko, data,  towar, stan_wyjsciowy):
        self.miasto = miasto 
        self.stoisko = stoisko
        self.data = data
        self.towar = towar
        self.stan_wyjsciowy = stan_wyjsciowy 

class Stoiska(db.Model):
    __tablename__ = 'stoiska'

    id = db.Column(db.Integer, primary_key=True)
    miasto = db.Column(db.String(99), nullable=False)
    stoisko = db.Column(db.String(99), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)
    

    def __init__(self, miasto, stoisko, lat,  lon):
        self.miasto = miasto 
        self.stoisko = stoisko
        self.lat = lat
        self.lon = lon