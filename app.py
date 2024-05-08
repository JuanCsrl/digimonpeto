from flask import Flask, render_template
import random
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models.digimon import Digimon  
from models.teams import PlayerTeam, StageTeam
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
   
    player_teams = PlayerTeam.query.all()
    if player_teams:
        random_player_team = random.choice(player_teams)
    stage_teams = StageTeam.query.all()
    if stage_teams:
        random_stage_teams = random.choice(stage_teams)
    return render_template('battle.html', player_team=random_player_team,stage_team=random_stage_teams)

if __name__ == '__main__':
    app.run(debug=True)
