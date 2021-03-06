"""add similar

Revision ID: 0bb69d222ea2
Revises: 43e51f930d79
Create Date: 2020-07-08 23:13:45.133765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0bb69d222ea2'
down_revision = '43e51f930d79'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'post', ['post_id'], ['id'])
        batch_op.drop_column('comment')

    with op.batch_alter_table('similar', schema=None) as batch_op:
        batch_op.add_column(sa.Column('post_id', sa.Integer(), nullable=True))
        batch_op.drop_index('ix_similar_name')
        batch_op.create_index(batch_op.f('ix_similar_name'), ['name'], unique=False)
        batch_op.create_foreign_key(None, 'post', ['post_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('similar', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_index(batch_op.f('ix_similar_name'))
        batch_op.create_index('ix_similar_name', ['name'], unique=1)
        batch_op.drop_column('post_id')

    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('comment', sa.VARCHAR(length=600), nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###
