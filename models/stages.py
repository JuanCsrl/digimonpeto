from extensions import db
class Stage(db.Model):
    __tablename__ = 'stage'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    nivel = db.Column(db.String(100), nullable=False)