"""Added path field

Revision ID: b640ad60d47e
Revises: 4c114d5be403
Create Date: 2020-07-19 14:48:20.946558

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b640ad60d47e'
down_revision = '4c114d5be403'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('file', sa.Column('path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('file', 'path')
    # ### end Alembic commands ###
