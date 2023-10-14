"""add_properties_to_vacations

Revision ID: 55d2cd89b0d6
Revises: d08a221775b4
Create Date: 2023-10-14 10:49:29.107577

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '55d2cd89b0d6'
down_revision = 'd08a221775b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vacation', 'type',
               existing_type=postgresql.ENUM('paid', 'unpaid', name='vacationtype'),
               nullable=False)
    op.alter_column('vacation', 'start_date',
               existing_type=sa.DATE(),
               nullable=False)
    op.alter_column('vacation', 'end_date',
               existing_type=sa.DATE(),
               nullable=False)
    op.alter_column('vacation', 'employee_id',
               existing_type=postgresql.UUID(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vacation', 'employee_id',
               existing_type=postgresql.UUID(),
               nullable=True)
    op.alter_column('vacation', 'end_date',
               existing_type=sa.DATE(),
               nullable=True)
    op.alter_column('vacation', 'start_date',
               existing_type=sa.DATE(),
               nullable=True)
    op.alter_column('vacation', 'type',
               existing_type=postgresql.ENUM('paid', 'unpaid', name='vacationtype'),
               nullable=True)
    # ### end Alembic commands ###