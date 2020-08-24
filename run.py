from flask import Flask
from flask_jwt import JWT
from security import authenticate, identity

def api_users(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    app.secret_key = "SECRET_KEY"
    jwt = JWT(app, authenticate, identity)
    
    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from Model import db
    db.init_app(app)

    return app


if __name__ == "__main__":
    app = api_users("config")
    app.run(host='0.0.0.0', debug=True)