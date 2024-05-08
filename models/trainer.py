from extensions import db
class Trainer(db.Model):
    __tablename__ = 'trainer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    affinity = db.Column(db.String(50))
    gender = db.Column(db.String(50))
    card = db.Column(db.LargeBinary)  
    