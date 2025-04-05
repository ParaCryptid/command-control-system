from flask import Flask
from .routes.example import example_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(example_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=False, host='0.0.0.0', port=8080)