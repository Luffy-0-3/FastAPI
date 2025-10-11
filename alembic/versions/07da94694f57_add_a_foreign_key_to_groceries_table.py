"""add a foreign key to groceries table

Revision ID: 07da94694f57
Revises: 6e224a4cfd2b
Create Date: 2025-10-11 00:01:25.097358

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '07da94694f57'
down_revision: Union[str, Sequence[str], None] = '6e224a4cfd2b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("groceries",sa.Column("user_id",sa.Integer(),nullable=False))
    op.create_foreign_key("post_user_fk",source_table="groceries",referent_table="users_data",
                          local_cols=["user_id"],remote_cols=["id"],ondelete="CASCADE")#remote_co id is user table id
    


def downgrade() -> None:
    op.drop_constraint("post_user_fk",table_name="groceries")
    op.drop_column("groceries","user_id")
