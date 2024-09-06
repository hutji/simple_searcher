import os

ELASTICSEARCH_URL = os.getenv("ELASTICSEARCH_URL", "http://localhost:9200")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///documents.db")
