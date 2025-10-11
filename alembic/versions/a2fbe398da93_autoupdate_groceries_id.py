"""autoupdate groceries id

Revision ID: a2fbe398da93
Revises: 07da94694f57
Create Date: 2025-10-11 00:20:19.209358

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a2fbe398da93'
down_revision: Union[str, Sequence[str], None] = '07da94694f57'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    # Create a sequence and link it to groceries.id for auto-increment behavior
    op.execute("""
        CREATE SEQUENCE IF NOT EXISTS groceries_id_seq OWNED BY groceries.id;
        ALTER TABLE groceries ALTER COLUMN id SET DEFAULT nextval('groceries_id_seq');
    """)


def downgrade() -> None:
    # Remove the default and drop the sequence if rolling back
    op.execute("""
        ALTER TABLE groceries ALTER COLUMN id DROP DEFAULT;
        DROP SEQUENCE IF EXISTS groceries_id_seq;
    """)