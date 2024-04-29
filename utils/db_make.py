import traceback

def preencher_banco_dados():
    from app import db
    from models.digimon import Digimon
    from models.trainer import Trainer
    from models.teams import StageTeam, PlayerTeam
    from models.stages import Stage
    try:
        # Criar alguns treinadores
        treinador1 = Trainer(nome='Ash')
        treinador2 = Trainer(nome='Misty')
        treinador3 = Trainer(nome='Brock')

        # Adicionar treinadores ao banco de dados
        db.session.add_all([treinador1, treinador2, treinador3])
        db.session.commit() 
        treinador1_id = treinador1.id
        treinador2_id = treinador2.id
        treinador3_id = treinador3.id

        # Criar alguns Digimons
        digimon1 = Digimon(nome='Agumon', nivel=5, vida=100, stamina=80, ataque=50, defesa=30, tipo='Fogo')
        digimon2 = Digimon(nome='Gabumon', nivel=6, vida=120, stamina=90, ataque=60, defesa=40, tipo='Água')
        digimon3 = Digimon(nome='Veemon', nivel=7, vida=150, stamina=100, ataque=70, defesa=50, tipo='Terra')

        # Adicionar Digimons ao banco de dados
        db.session.add_all([digimon1, digimon2, digimon3])

        # Criar algumas equipes de jogadores
        equipe_jogador1 = PlayerTeam(trainer_id=treinador1_id, digimon1_id=1, digimon2_id=2, digimon3_id=3, team_status='ativo')
        equipe_jogador2 = PlayerTeam(trainer_id=treinador2_id, digimon1_id=2, digimon2_id=3, digimon3_id=1, team_status='inativo')
        equipe_jogador3 = PlayerTeam(trainer_id=treinador3_id, digimon1_id=3, digimon2_id=1, digimon3_id=2, team_status='ativo')

        # Adicionar equipes de jogadores ao banco de dados
        db.session.add_all([equipe_jogador1, equipe_jogador2, equipe_jogador3])

        # Criar algumas fases
        fase1 = Stage(nome='Floresta', dificuldade='Fácil')
        fase2 = Stage(nome='Montanha', dificuldade='Média')
        fase3 = Stage(nome='Caverna', dificuldade='Difícil')

        # Adicionar fases ao banco de dados
        db.session.add_all([fase1, fase2, fase3])

        # Criar algumas equipes de fase
        equipe_fase1 = StageTeam(stage_id=1, digimon1_id=1, digimon2_id=2, digimon3_id=3, team_status='ativo')
        equipe_fase2 = StageTeam(stage_id=2, digimon1_id=2, digimon2_id=3, digimon3_id=1, team_status='inativo')
        equipe_fase3 = StageTeam(stage_id=3, digimon1_id=3, digimon2_id=1, digimon3_id=2, team_status='ativo')

        # Adicionar equipes de fase ao banco de dados
        db.session.add_all([equipe_fase1, equipe_fase2, equipe_fase3])

        # Confirmar as alterações
        db.session.commit()

    except Exception as e:
        # Em caso de erro, desfazer as alterações
        db.session.rollback()
        print(f"Ocorreu um erro ao preencher o banco de dados: {str(e)}") #\n trace: {traceback.format_exc()}")
