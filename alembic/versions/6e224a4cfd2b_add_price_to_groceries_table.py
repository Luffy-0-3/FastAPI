"""add price to groceries table

Revision ID: 6e224a4cfd2b
Revises: 81853e259505
Create Date: 2025-10-10 23:54:43.809485

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6e224a4cfd2b'
down_revision: Union[str, Sequence[str], None] = '81853e259505'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("groceries", sa.Column("price", sa.Float(), nullable=False))
    op.add_column("groceries", sa.Column("quantity", sa.Integer(), nullable=False))


def downgrade() -> None:
    op.drop_column("groceries","price")
    op.drop_column("groceries","quantity")
    
