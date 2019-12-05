"""add solution table

Revision ID: 9c2114545fec
Revises: f68d8d207632
Create Date: 2019-12-04 21:06:39.269238

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c2114545fec'
down_revision = 'f68d8d207632'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('solution',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('posted_by', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('posted_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('solution')
    # ### end Alembic commands ###