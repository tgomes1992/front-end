"""adding website

Revision ID: 40a0b275d515
Revises: 6c7315b6e181
Create Date: 2020-06-03 02:25:14.448773

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40a0b275d515'
down_revision = '6c7315b6e181'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('website', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'website')
    # ### end Alembic commands ###
