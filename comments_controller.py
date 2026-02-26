from flask import Blueprint, request, jsonify
from .comment_model import comments, Comment 

comments_bp = Blueprint("comments", __name__, url_prefix="/comments")

# ESTA ROTA PRECISA RETORNAR O JSON, NÃO O TEXTO "API FUNCIONANDO"
@comments_bp.get("/")
def get_comments():
    return jsonify([
        {
            "id": c.id,
            "content": c.content,
            "author": c.author,
            "created_at": c.created_at.isoformat()
        }
        for c in comments
    ]), 200

@comments_bp.post("/")
def create_comment():
    data = request.get_json() or {}
    new_comment = Comment(
        content=data.get("content"),
        author=data.get("author")
    )
    comments.append(new_comment)
    return jsonify({"message": "Criado!"}), 201

@comments_bp.delete("/<int:comment_id>")
def delete_comment(comment_id):
    for c in comments:
        if c.id == comment_id:
            comments.remove(c)
            return jsonify({"message": "Removido!"}), 200
    return jsonify({"error": "Erro"}), 404