from flask import Blueprint, request, jsonify
from .comment_model import comments, Comment   # import relativo correto

# cria blueprint
comments_bp = Blueprint("comments", __name__, url_prefix="/comments")


# ==== CREATE ====
@comments_bp.post("/")
def create_comment():
    data = request.get_json() or {}

    new_comment = Comment(
        content=data.get("content"),
        author=data.get("author")
    )

    comments.append(new_comment)

    return jsonify({
        "message": "Comentário criado com sucesso!",
        "id": new_comment.id
    }), 201


# ==== READ ALL ====
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


# ==== READ ONE ====
@comments_bp.get("/<int:comment_id>")
def get_comment(comment_id):
    for c in comments:
        if c.id == comment_id:
            return jsonify({
                "id": c.id,
                "content": c.content,
                "author": c.author,
                "created_at": c.created_at.isoformat()
            }), 200

    return jsonify({"error": "Comentário não encontrado"}), 404


# ==== UPDATE ====
@comments_bp.put("/<int:comment_id>")
def update_comment(comment_id):
    data = request.get_json() or {}

    for c in comments:
        if c.id == comment_id:
            c.content = data.get("content", c.content)
            c.author = data.get("author", c.author)
            return jsonify({"message": "Comentário atualizado com sucesso!"}), 200

    return jsonify({"error": "Comentário não encontrado"}), 404


# ==== DELETE ====
@comments_bp.delete("/<int:comment_id>")
def delete_comment(comment_id):
    for c in comments:
        if c.id == comment_id:
            comments.remove(c)
            return jsonify({"message": "Comentário removido com sucesso!"}), 200

    return jsonify({"error": "Comentário não encontrado"}), 404
@comments_bp.route("/")
def home():
    return "API funcionando via blueprint 🟢"
