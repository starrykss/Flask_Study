"""empty message

Revision ID: 9434fa70edf2
Revises: 0bd40f090209
Create Date: 2023-08-28 14:14:02.951901

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9434fa70edf2'
down_revision = '0bd40f090209'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###
