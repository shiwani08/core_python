from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os
from pymongo.errors import ConnectionFailure
from controllers.auth_controller import auth_bp
from controllers.main_controller import main_bp

load_dotenv()

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv('SECRET_KEY', 'supersecretkey')
    app.config['MONGO_URI'] = os.getenv('MONGODB_URI')

    # Initialize MongoDB
    mongo.init_app(app)

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    try:
        mongo.cx.server_info()
        print("✅ Connected to MongoDB successfully.")
    except ConnectionFailure as e:
        print(f"❌ Could not connect to MongoDB: {e}")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
