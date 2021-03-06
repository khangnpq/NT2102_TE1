"""Initial commit

Revision ID: 3f9d699beb4a
Revises: 
Create Date: 2021-02-03 15:36:41.326010

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f9d699beb4a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('participant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=36), nullable=True),
    sa.Column('last_name', sa.String(length=84), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('image_name', sa.String(length=36), nullable=True),
    sa.Column('lottery_code', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('participant')
    # ### end Alembic commands ###
