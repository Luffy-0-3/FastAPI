"""add users_data table

Revision ID: 81853e259505
Revises: db445fa7b31b
Create Date: 2025-10-10 23:02:31.795654

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '81853e259505'
down_revision: Union[str, Sequence[str], None] = 'db445fa7b31b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("users_data",
                    sa.Column("id",sa.Integer(),nullable=False,primary_key=True,autoincrement=True),
                    sa.Column("email",sa.String(),nullable=False),
                    sa.Column("password",sa.String(),nullable=False),
                    sa.Column("created_at",sa.TIMESTAMP(timezone=True),server_default=sa.text("now()"),nullable=False),
                    sa.UniqueConstraint("email")
                      )
    pass


def downgrade() -> None:
    op.drop_table("users_data")
    pass