"""empty message

Revision ID: b10b968b388b
Revises: 89b70aa7faf7
Create Date: 2024-04-29 16:30:30.448770

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b10b968b388b'
down_revision = '89b70aa7faf7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('digimon', schema=None) as batch_op:
        batch_op.add_column(sa.Column('card', sa.LargeBinary(), nullable=True))
        batch_op.add_column(sa.Column('sprit', sa.LargeBinary(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('digimon', schema=None) as batch_op:
        batch_op.drop_column('sprit')
        batch_op.drop_column('card')

    # ### end Alembic commands ###
