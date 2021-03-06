"""add model similar

Revision ID: d80741809f7f
Revises: 32282709bb58
Create Date: 2020-07-03 16:41:56.498849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd80741809f7f'
down_revision = '32282709bb58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('similar',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_similar_name'), 'similar', ['name'], unique=True)
    op.create_foreign_key(None, 'comment', 'post', ['post_id'], ['id'])
    op.drop_column('comment', 'comment')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('comment', sa.VARCHAR(length=600), nullable=True))
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.drop_index(op.f('ix_similar_name'), table_name='similar')
    op.drop_table('similar')
    # ### end Alembic commands ###
