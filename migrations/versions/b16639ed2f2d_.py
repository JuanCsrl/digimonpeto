"""empty message

Revision ID: b16639ed2f2d
Revises: 74e53ae36772
Create Date: 2024-04-29 17:48:33.249871

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b16639ed2f2d'
down_revision = '74e53ae36772'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trainer', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
        batch_op.alter_column('affinity',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=50),
               nullable=True)
        batch_op.alter_column('gender',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=50),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trainer', schema=None) as batch_op:
        batch_op.alter_column('gender',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=100),
               nullable=False)
        batch_op.alter_column('affinity',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=100),
               nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)

    # ### end Alembic commands ###
