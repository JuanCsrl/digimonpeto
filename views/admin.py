from flask import Blueprint, render_template, redirect, url_for, request
from extensions import db
from models.digimon import Digimon
from models.trainer import Trainer
import os
 # Importe o objeto app do arquivo app.py

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


# Rota para a página de administração
@admin_bp.route('/')
def admin_index():
    return render_template('admin.html')

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
        # Processar o formulário e cadastrar o novo Trainer no banco de dados
        # Exemplo:
        if 'card' in request.files:
            # Salva os arquivos em um diretório de uploads
            card_file = request.files['card']
            card_path = os.path.join(app.config['UPLOAD_FOLDER'], card_file.filename)
            card_file.save(card_path)

            new_trainer = Trainer(name=request.form['nome'],
                                  affinity=request.form['afinidade'],
                                  gender=request.form['genero'],
                                  card = card_path
                                  
                                  )
            db.session.add(new_trainer)
            db.session.commit()
        return redirect(url_for('admin.admin_index'))

# Adicione rotas para cadastrar novas entidades conforme necessário
