from flask import Flask
from config import Config
from routes.home import home_bp
from routes.auth import auth_bp

# Indicamos 'template' porque tu carpeta está en singular
app = Flask(__name__, template_folder='template', static_folder='static')
app.config.from_object(Config)

# Registrar los Blueprints de routes/
app.register_blueprint(home_bp)
app.register_blueprint(auth_bp)


if __name__ == '__main__':
    app.run(debug=True)