"""empty message

Revision ID: 92f0840eed4c
Revises: 
Create Date: 2019-04-01 18:36:13.556510

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92f0840eed4c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('first_player_name', sa.String(), nullable=False),
    sa.Column('second_player_name', sa.String(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_team_id'), 'team', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_team_id'), table_name='team')
    op.drop_table('team')
    # ### end Alembic commands ###