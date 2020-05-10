"""update database

Revision ID: fedc467a3226
Revises: fd44082b2246
Create Date: 2020-05-10 21:49:35.274116

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fedc467a3226'
down_revision = 'fd44082b2246'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('date_posted', sa.DateTime(), nullable=False))
    op.alter_column('blogs', 'description',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.drop_index('ix_blogs_description', table_name='blogs')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_blogs_description', 'blogs', ['description'], unique=False)
    op.alter_column('blogs', 'description',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.drop_column('blogs', 'date_posted')
    # ### end Alembic commands ###
