"""add groceries table

Revision ID: abc11dbbf6e6
Revises: 
Create Date: 2025-10-10 22:25:52.610321

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'abc11dbbf6e6'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("groceries",sa.Column("id",sa.Integer(),nullable=False,primary_key=True),
                    sa.Column("name",sa.String(),nullable=False)) 
    pass


def downgrade() -> None:
    op.drop_table("groceries")
    pass
