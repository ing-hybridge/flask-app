class Config:
    # Reemplaza con tus credenciales reales:
    # postgresql://usuario:password@host:puerto/base
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg://postgres:mysecretpassword@localhost:5435/flask_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'tu_clave_secreta_aqui'