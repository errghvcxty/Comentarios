from flask import Flask, render_template
from .comments_controller import comments_bp

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template("index.html")  # <-- aqui chamamos o template

    # registra a blueprint de comentários
    app.register_blueprint(comments_bp)

    return app
