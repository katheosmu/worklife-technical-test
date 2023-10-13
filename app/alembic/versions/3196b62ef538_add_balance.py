"""add_vacation_table

Revision ID: 3196b62ef538
Revises: 27bf2aa3b8c7
Create Date: 2023-10-12 10:39:59.317990

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3196b62ef538'
down_revision = '27bf2aa3b8c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employee', sa.Column('balance', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('employee', 'balance')
    # ### end Alembic commands ###
