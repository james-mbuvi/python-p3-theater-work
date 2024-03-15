"""Create auditions and roles tables

Revision ID: 7e96e51f61e8
Revises: 
Create Date: 2024-03-15 12:02:58.578845

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e96e51f61e8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    
    op.drop_column('auditions', 'phone')

    
    op.add_column('auditions', sa.Column('role_id', sa.Integer(), nullable=True))
    op.create_foreign_key(
        'fk_role_id',
        'auditions',
        'roles',
        ['role_id'],
        ['id'],
    )
    pass


def downgrade():
    op.add_column('auditions', sa.Column('phone', sa.Integer(), nullable=True))

    
    op.drop_column('auditions', 'role_id')
    op.drop_constraint('fk_role_id', 'auditions', type_='foreignkey')
    pass
