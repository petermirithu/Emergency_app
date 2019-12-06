"""update emergency table

Revision ID: dcf1d8609283
Revises: 9c2114545fec
Create Date: 2019-12-05 13:06:06.001250

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dcf1d8609283'
down_revision = '9c2114545fec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('emergency', sa.Column('latitude', sa.String(length=255), nullable=True))
    op.add_column('emergency', sa.Column('longitude', sa.String(length=255), nullable=True))
    op.drop_column('emergency', 'location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('emergency', sa.Column('location', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('emergency', 'longitude')
    op.drop_column('emergency', 'latitude')
    # ### end Alembic commands ###