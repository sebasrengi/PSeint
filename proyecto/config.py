import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave-secreta-cosmeticos-2026'
    # Placeholder de conexión (PostgreSQL o SQLite)
    DB_HOST = os.environ.get('DB_HOST') or 'localhost'
    DB_NAME = os.environ.get('DB_NAME') or 'inventario_cosmeticos'
    DB_USER = os.environ.get('DB_USER') or 'postgres'
    DB_PASS = os.environ.get('DB_PASS') or 'admin123'