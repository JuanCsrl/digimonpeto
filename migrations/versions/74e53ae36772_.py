"""empty message

Revision ID: 74e53ae36772
Revises: bef0c1985e22
Create Date: 2024-04-29 17:45:21.311603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74e53ae36772'
down_revision = 'bef0c1985e22'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trainer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('card', sa.LargeBinary(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trainer', schema=None) as batch_op:
        batch_op.drop_column('card')

    # ### end Alembic commands ###