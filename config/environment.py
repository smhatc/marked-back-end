import os

db_URI = os.getenv("DATABASE_URL")

if db_URI and db_URI.startswith("postgres://"):
    db_URI = db_URI.replace("postgres://", "postgresql://", 1)

jwt_secret = os.getenv("JWT_SECRET")
