from flask import Blueprint, render_template, redirect, url_for, request
from extensions import db
from models.digimon import Digimon
from models.trainer import Trainer
from models.teams import PlayerTeam, StageTeam
from models.stages import Stage
import os
 # Importe o objeto app do arquivo app.py

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


# Rota para a página de administração
@admin_bp.route('/')
def admin_index():
    digimons = Digimon.query.all()
    tamers = Trainer.query.all()
    stages= Stage.query.all()
    return render_template('admin.html', digimons=digimons, trainers=tamers, stages=stages)

# Rota para cadastrar um novo Digimon
@admin_bp.route('/cadastrar_digimon', methods=['POST'])
def cadastrar_digimon():
    from app import app 
    if request.method == 'POST':
        # Processar o formulário e cadastrar o novo Digimon no banco de dados
        # Exemplo:
        if 'card' in request.files and 'sprite' in request.files:
            # Salva os arquivos em um diretório de uploads
            card_file = request.files['card']
            card_path = os.path.join(app.config['UPLOAD_FOLDER'], card_file.filename)
            card_file.save(card_path)

            sprite_file = request.files['sprite']
            sprite_path = os.path.join(app.config['UPLOAD_FOLDER'], sprite_file.filename)
            sprite_file.save(sprite_path)

            new_digimon = Digimon(name=request.form['nome'],
            nivel=request.form['nivel'],
            life=request.form['vida'],
            stamina=request.form['stamina'],
            atk=request.form['ataque'],
            defense=request.form['defesa'],
            type=request.form['tipo'],
            lore=request.form['historia'],
            card=card_path,
            sprite=sprite_path,
            )
            db.session.add(new_digimon)
            db.session.commit()
        return redirect(url_for('admin.admin_index'))

# Rota para cadastrar um novo Trainer
@admin_bp.route('/cadastrar_trainer', methods=['POST'])
def cadastrar_trainer():
    from app import app 
    if request.method == 'POST':
        if 'card' in request.files:
            card_file = request.files['card']
            # Leia o conteúdo do arquivo como dados binários
            card_data = card_file.read()

            # Crie um novo objeto Trainer e configure o campo do cartão com os dados binários
            new_trainer = Trainer(name=request.form['nome'],
                                  affinity=request.form['afinidade'],
                                  gender=request.form['genero'],
                                  card=card_data  # Salve os dados binários diretamente no campo do cartão
                                  )
            db.session.add(new_trainer)
            db.session.commit()

        return redirect(url_for('admin.admin_index'))
# Adicione rotas para cadastrar novas entidades conforme necessário

@admin_bp.route('/cadastrar_player_team', methods=['POST'])
def cadastrar_player_team():
    from app import app 
    if request.method == 'POST':
       new_player_team = PlayerTeam(
           trainer_id=request.form['trainer_id'],
           digimon1_id=request.form['digimon1_id'],
           digimon2_id=request.form['digimon2_id'], 
           digimon3_id=request.form['digimon3_id'],
       )
       db.session.add(new_player_team)
       db.session.commit()
    return redirect(url_for('admin.admin_index'))

@admin_bp.route('/cadastrar_stage', methods=['POST'])
def cadastrar_stage():
    if request.method == 'POST':
        # Processar o formulário e cadastrar a nova Stage no banco de dados
        new_stage = Stage(
            name=request.form['name'],
            nivel=request.form['nivel']
            # Adicione outros campos conforme necessário
        )
        db.session.add(new_stage)
        db.session.commit()
    return redirect(url_for('admin.admin_index'))

@admin_bp.route('/cadastrar_stage_team', methods=['POST'])
def cadastrar_stage_team():
    if request.method == 'POST':
        # Processar o formulário e cadastrar a nova StageTeam no banco de dados
        new_stage_team = StageTeam(
            stage_id=request.form['stage_id'],
            digimon1_id=request.form['digimon1_id'],
            digimon2_id=request.form['digimon2_id'],
            digimon3_id=request.form['digimon3_id'],
            team_status=request.form['team_status']
            # Adicione outros campos conforme necessário
        )
        db.session.add(new_stage_team)
        db.session.commit()
    return redirect(url_for('admin.admin_index'))
