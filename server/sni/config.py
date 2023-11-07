import os
from typing import List

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
load_dotenv(os.path.join(basedir, ".env"))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CACHE_NO_NULL_WARNING = os.environ.get("CACHE_NO_NULL_WARNING", True)

    CSRF_ENABLED = True


def string_literal_check(lst: List[str]) -> str:
    check = ", ".join([f"'{item}'" for item in lst])
    return f"({check})"


ALLOWED_LOCALES = [
    "ar",
    "de",
    "en",
    "es",
    "fa",
    "fi",
    "fr",
    "he",
    "it",
    "pt",
    "ru",
    "zh",
]
ALLOWED_FORMATS = ["pdf", "epub", "mobi", "txt"]
