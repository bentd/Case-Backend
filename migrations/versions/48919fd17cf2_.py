"""empty message

Revision ID: 48919fd17cf2
Revises: 
Create Date: 2017-09-24 22:25:37.567936

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '48919fd17cf2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'confirmed',
               existing_type=mysql.DATETIME(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'confirmed',
               existing_type=mysql.DATETIME(),
               nullable=True)
    # ### end Alembic commands ###
