"""Initial creation

Revision ID: 825a38237015
Revises: 
Create Date: 2023-03-19 16:17:33.254683

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey

# revision identifiers, used by Alembic.
revision = '825a38237015'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'cheese',
        Column('id', Integer, primary_key=True),
        Column('type_id', Integer, ForeignKey('cheese_type.id')),
        Column('creation_date', Date, nullable=False),
    )

    op.create_table(
        'cheese_type',
        Column('id', Integer, primary_key=True),
        Column('name', String(50), nullable=False)
    )

    op.create_table(
        'queso_blanco',
        Column('id', Integer, primary_key=True),
        Column('cheese_id', Integer, ForeignKey('cheese.id')),
        Column('milk_liters', Float),
        Column('final_weight_grams', Integer),
        Column('vinegar_milliliters', Integer),
        Column('salt_milliliters', Integer),
        Column('pasteurisation_celcius', Integer)
    )

    op.create_table(
        'brie',
        Column('id', Integer, primary_key=True),
        Column('cheese_id', Integer, ForeignKey('cheese.id')),
        Column('pasteurisation_celcius', Integer)
    )

    op.create_table(
        'mozzarella',
        Column('id', Integer, primary_key=True),
        Column('cheese_id', Integer, ForeignKey('cheese.id')),
        Column('milk_liters', Float),
        Column('final_weight_grams', Integer),
        Column('salt_milliliters', Integer),
        Column('pasteurisation_celcius', Integer)
    )


def downgrade() -> None:
    op.drop_table('mozzarella')
    op.drop_table('brie')
    op.drop_table('queso_blanco')
    op.drop_table('cheese_type')
    op.drop_table('cheese')
