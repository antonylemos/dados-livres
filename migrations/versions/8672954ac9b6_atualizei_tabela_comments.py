"""atualizei tabela comments

Revision ID: 8672954ac9b6
Revises: 7ad2e5a1132d
Create Date: 2020-08-19 02:00:08.631017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8672954ac9b6'
down_revision = '7ad2e5a1132d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('username', sa.String(length=200), nullable=True))
        batch_op.create_index(batch_op.f('ix_comment_username'), ['username'], unique=False)
        batch_op.drop_index('ix_comment_email')
        batch_op.drop_index('ix_comment_name')
        batch_op.create_foreign_key(batch_op.f('fk_comment_user_id_user'), 'user', ['user_id'], ['id'])
        batch_op.drop_column('name')
        batch_op.drop_column('email')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.VARCHAR(length=200), nullable=True))
        batch_op.add_column(sa.Column('name', sa.VARCHAR(length=200), nullable=True))
        batch_op.drop_constraint(batch_op.f('fk_comment_user_id_user'), type_='foreignkey')
        batch_op.create_index('ix_comment_name', ['name'], unique=False)
        batch_op.create_index('ix_comment_email', ['email'], unique=False)
        batch_op.drop_index(batch_op.f('ix_comment_username'))
        batch_op.drop_column('username')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
