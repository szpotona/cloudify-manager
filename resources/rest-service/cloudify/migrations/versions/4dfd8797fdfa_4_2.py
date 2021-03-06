""" (4.2) Add resource_availability property to a resource

Revision ID: 4dfd8797fdfa
Revises: 3496c876cd1a
Create Date: 2017-09-27 15:57:27.933008

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy.dialects import postgresql  # Adding this manually

# revision identifiers, used by Alembic.
revision = '4dfd8797fdfa'
down_revision = '3496c876cd1a'
branch_labels = None
depends_on = None


def upgrade():
    # Adding the enum resource_availability to postgres
    resource_availability = postgresql.ENUM('private', 'tenant', 'global',
                                            name='resource_availability')
    resource_availability.create(op.get_bind())

    # add_column of resource_availability was changed manually
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blueprints', sa.Column('resource_availability', resource_availability, nullable=True))
    op.add_column('deployment_modifications', sa.Column('resource_availability', resource_availability, nullable=True))
    op.add_column('deployment_update_steps', sa.Column('resource_availability', resource_availability, nullable=True))
    op.add_column('deployment_updates', sa.Column('resource_availability', resource_availability, nullable=True))
    op.add_column('deployments', sa.Column('resource_availability', resource_availability, nullable=True))
    op.add_column('events', sa.Column('resource_availability', resource_availability, nullable=True))
    op.add_column('executions', sa.Column('resource_availability', resource_availability, nullable=True))
    op.add_column('logs', sa.Column('resource_availability', resource_availability, nullable=True))
    op.add_column('node_instances', sa.Column('resource_availability', resource_availability, nullable=True))
    op.add_column('nodes', sa.Column('resource_availability', resource_availability, nullable=True))
    op.add_column('plugins', sa.Column('resource_availability', resource_availability, nullable=True))
    op.add_column('secrets', sa.Column('resource_availability', resource_availability, nullable=True))
    op.add_column('snapshots', sa.Column('resource_availability', resource_availability, nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('snapshots', 'resource_availability')
    op.drop_column('secrets', 'resource_availability')
    op.drop_column('plugins', 'resource_availability')
    op.drop_column('nodes', 'resource_availability')
    op.drop_column('node_instances', 'resource_availability')
    op.drop_column('logs', 'resource_availability')
    op.drop_column('executions', 'resource_availability')
    op.drop_column('events', 'resource_availability')
    op.drop_column('deployments', 'resource_availability')
    op.drop_column('deployment_updates', 'resource_availability')
    op.drop_column('deployment_update_steps', 'resource_availability')
    op.drop_column('deployment_modifications', 'resource_availability')
    op.drop_column('blueprints', 'resource_availability')
    # ### end Alembic commands ###

    # Removing the enum resource_availability from postgres
    resource_availability = postgresql.ENUM('private', 'tenant', 'global',
                                            name='resource_availability')
    resource_availability.drop(op.get_bind())
