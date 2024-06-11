"""Add Turkish language

Revision ID: 006948e4f251
Revises: 827c107609c5
Create Date: 2024-05-21 15:27:23.855007

"""

from typing import Sequence, Union

from alembic import op
from alembic_postgresql_enum import TableReference

# revision identifiers, used by Alembic.
revision: str = "006948e4f251"
down_revision: Union[str, None] = "827c107609c5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.sync_enum_values(
        "public",
        "locales",
        [
            "ar",
            "de",
            "en",
            "es",
            "fa",
            "fi",
            "fr",
            "he",
            "it",
            "ko",
            "pt-br",
            "ru",
            "tr",
            "vi",
            "zh-cn",
        ],
        [
            TableReference(
                table_schema="public",
                table_name="document_translations",
                column_name="locale",
            ),
            TableReference(
                table_schema="public",
                table_name="blog_post_translations",
                column_name="locale",
            ),
            TableReference(
                table_schema="public",
                table_name="blog_series_translations",
                column_name="locale",
            ),
        ],
        enum_values_to_rename=[],
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.sync_enum_values(
        "public",
        "locales",
        [
            "ar",
            "de",
            "en",
            "es",
            "fa",
            "fi",
            "fr",
            "he",
            "it",
            "ko",
            "pt-br",
            "ru",
            "vi",
            "zh-cn",
        ],
        [
            TableReference(
                table_schema="public",
                table_name="document_translations",
                column_name="locale",
            ),
            TableReference(
                table_schema="public",
                table_name="blog_post_translations",
                column_name="locale",
            ),
            TableReference(
                table_schema="public",
                table_name="blog_series_translations",
                column_name="locale",
            ),
        ],
        enum_values_to_rename=[],
    )
    # ### end Alembic commands ###
