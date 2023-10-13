"""add_one_to_many_relationship

Revision ID: d08a221775b4
Revises: 3b328caadefa
Create Date: 2023-10-12 11:32:18.551580

"""
from alembic import op
import sqlalchemy as sa

from app.model.base import CustomUUID

# revision identifiers, used by Alembic.
revision = 'd08a221775b4'
down_revision = '3b328caadefa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vacation', sa.Column('employee_id', CustomUUID(), nullable=True))
    op.create_foreign_key(None, 'vacation', 'employee', ['employee_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'vacation', type_='foreignkey')
    op.drop_column('vacation', 'employee_id')
    # ### end Alembic commands ###