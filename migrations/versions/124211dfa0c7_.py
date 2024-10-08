"""empty message

Revision ID: 124211dfa0c7
Revises: 6678beea847f
Create Date: 2024-08-21 17:45:08.869984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '124211dfa0c7'
down_revision = '6678beea847f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=20), nullable=False),
    sa.Column('last_name', sa.String(length=20), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profile')
    # ### end Alembic commands ###
