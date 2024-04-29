from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models.digimon import Digimon  
from extensions import db
from views.admin import admin_bp  # Importe as views de admin
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///digimons.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TEMPLATE_FOLDER'] = 'views/templates'

db.init_app(app)  
migrate = Migrate(app, db)
app.register_blueprint(admin_bp)

@app.route('/')
def index():
   
    digimons = Digimon.query.all()
    return render_template('battle.html', digimons=digimons)

if __name__ == '__main__':
    app.run(debug=True)
