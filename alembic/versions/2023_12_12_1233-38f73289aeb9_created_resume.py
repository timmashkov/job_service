"""created resume

Revision ID: 38f73289aeb9
Revises: 
Create Date: 2023-12-12 12:33:42.784348

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "38f73289aeb9"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "resume",
        sa.Column("first_name", sa.String(length=20), nullable=False),
        sa.Column("last_name", sa.String(length=20), nullable=False),
        sa.Column("age", sa.Integer(), nullable=False),
        sa.Column("about", sa.Text(), nullable=True),
        sa.Column("experience", sa.Integer(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("(CURRENT_TIMESTAMP)"),
            nullable=False,
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("resume")
    # ### end Alembic commands ###
