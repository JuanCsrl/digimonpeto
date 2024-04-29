from extensions import db
class Digimon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    nivel = db.Column(db.Integer)
    life = db.Column(db.Integer)
    stamina = db.Column(db.Integer)
    atk = db.Column(db.Integer)
    defense = db.Column(db.Integer)
    type = db.Column(db.String(100))
    lore = db.Column(db.String(1000))
    card = db.Column(db.LargeBinary)  
    sprite = db.Column(db.LargeBinary) 
