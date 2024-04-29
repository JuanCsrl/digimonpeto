from extensions import db
class PlayerTeam(db.Model):
    __tablename__ = 'player_team'

    id = db.Column(db.Integer, primary_key=True)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainer.id'))
    digimon1_id = db.Column(db.Integer, db.ForeignKey('digimon.id'))
    digimon2_id = db.Column(db.Integer, db.ForeignKey('digimon.id'))
    digimon3_id = db.Column(db.Integer, db.ForeignKey('digimon.id'))
    
    # Adicione campos para os status da equipe
    team_status = db.Column(db.String(50))  # Por exemplo, "ativo", "inativo", etc.

    # Define os relacionamentos com as tabelas de Trainer e Digimon
    trainer = db.relationship('Trainer', backref='team_players')
    digimon1 = db.relationship('Digimon', foreign_keys=[digimon1_id])
    digimon2 = db.relationship('Digimon', foreign_keys=[digimon2_id])
    digimon3 = db.relationship('Digimon', foreign_keys=[digimon3_id])

    digimon1_life = db.Column(db.Integer)  # Vida do Digimon 1
    digimon1_stamina = db.Column(db.Integer)  # Stamina do Digimon 1
    digimon1_level = db.Column(db.Integer)  # Nível do Digimon 1
    digimon1_attack = db.Column(db.Integer)  # Ataque do Digimon 1
    digimon1_defense = db.Column(db.Integer)  # Defesa do Digimon 1
    digimon1_type = db.Column(db.String(50))  # Tipo do Digimon 1

    digimon2_life = db.Column(db.Integer)  # Vida do Digimon 2
    digimon2_stamina = db.Column(db.Integer)  # Stamina do Digimon 2
    digimon2_level = db.Column(db.Integer)  # Nível do Digimon 2
    digimon2_attack = db.Column(db.Integer)  # Ataque do Digimon 2
    digimon2_defense = db.Column(db.Integer)  # Defesa do Digimon 2
    digimon2_type = db.Column(db.String(50))  # Tipo do Digimon 2

    digimon3_life = db.Column(db.Integer)  # Vida do Digimon 3
    digimon3_stamina = db.Column(db.Integer)  # Stamina do Digimon 3
    digimon3_level = db.Column(db.Integer)  # Nível do Digimon 3
    digimon3_attack = db.Column(db.Integer)  # Ataque do Digimon 3
    digimon3_defense = db.Column(db.Integer)  # Defesa do Digimon 3
    digimon3_type = db.Column(db.String(50))  # Tipo do Digimon 3



class StageTeam(db.Model):
    __tablename__ = 'stage_team'

    id = db.Column(db.Integer, primary_key=True)
    stage_id = db.Column(db.Integer, db.ForeignKey('stage.id'))
    digimon1_id = db.Column(db.Integer, db.ForeignKey('digimon.id'))
    digimon2_id = db.Column(db.Integer, db.ForeignKey('digimon.id'))
    digimon3_id = db.Column(db.Integer, db.ForeignKey('digimon.id'))
    
    # Adicione campos para os status da equipe
    team_status = db.Column(db.String(50))

    # Define o relacionamento com a tabela de Stage
    stage = db.relationship('Stage', backref='stage_teams')

    # Define os relacionamentos com as tabelas de Digimon para acessar os status dos Digimons
    digimon1 = db.relationship('Digimon', foreign_keys=[digimon1_id])
    digimon2 = db.relationship('Digimon', foreign_keys=[digimon2_id])
    digimon3 = db.relationship('Digimon', foreign_keys=[digimon3_id])

    # Adicione campos para os status dos Digimons
    digimon1_life = db.Column(db.Integer)  # Vida do Digimon 1
    digimon1_stamina = db.Column(db.Integer)  # Stamina do Digimon 1
    digimon1_level = db.Column(db.Integer)  # Nível do Digimon 1
    digimon1_attack = db.Column(db.Integer)  # Ataque do Digimon 1
    digimon1_defense = db.Column(db.Integer)  # Defesa do Digimon 1
    digimon1_type = db.Column(db.String(50))  # Tipo do Digimon 1

    digimon2_life = db.Column(db.Integer)  # Vida do Digimon 2
    digimon2_stamina = db.Column(db.Integer)  # Stamina do Digimon 2
    digimon2_level = db.Column(db.Integer)  # Nível do Digimon 2
    digimon2_attack = db.Column(db.Integer)  # Ataque do Digimon 2
    digimon2_defense = db.Column(db.Integer)  # Defesa do Digimon 2
    digimon2_type = db.Column(db.String(50))  # Tipo do Digimon 2

    digimon3_life = db.Column(db.Integer)  # Vida do Digimon 3
    digimon3_stamina = db.Column(db.Integer)  # Stamina do Digimon 3
    digimon3_level = db.Column(db.Integer)  # Nível do Digimon 3
    digimon3_attack = db.Column(db.Integer)  # Ataque do Digimon 3
    digimon3_defense = db.Column(db.Integer)  # Defesa do Digimon 3
    digimon3_type = db.Column(db.String(50))  # Tipo do Digimon 3
