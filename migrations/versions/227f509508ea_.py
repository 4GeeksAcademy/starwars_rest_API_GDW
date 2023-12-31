"""empty message

Revision ID: 227f509508ea
Revises: b9fa8cd7cca1
Create Date: 2023-10-16 15:07:44.106833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '227f509508ea'
down_revision = 'b9fa8cd7cca1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.Column('vehicle_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['favorite_characters.id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['favorite_planets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['vehicle_id'], ['favorite_vehicles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorites')
    # ### end Alembic commands ###
