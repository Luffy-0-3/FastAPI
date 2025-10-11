"""add description column to groceries table

Revision ID: db445fa7b31b
Revises: abc11dbbf6e6
Create Date: 2025-10-10 22:45:38.434284

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'db445fa7b31b'
down_revision: Union[str, Sequence[str], None] = 'abc11dbbf6e6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("groceries",sa.Column("description",sa.String(),nullable=False))
    

def downgrade() -> None:
    op.drop_column("groceries","description")



# name = Column(String,nullable=False)
#     description = Column(String,nullable=False)
#     price = Column(Float,nullable=False)
#     quantity = Column(Integer,nullable=False)
#     user_id = Column(Integer,ForeignKey("users_data.id",ondelete="CASCADE"),nullable=False)
