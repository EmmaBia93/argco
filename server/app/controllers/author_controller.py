from app.extensions import db
from app.models.author import Author
from flask import request, jsonify

def get_all_authors():
    
    try:
        authors = Author.query.all()
        authors_data = [author.to_dict() for author in authors]

        return jsonify(authors_data), 200
    
    except Exception as e:
       return jsonify({'error': 'Internal server error', 'details': str(e)}), 500
   
def get_author_by_id(id):
    try:
       id = int(id)
    except ValueError:
        return jsonify({"error": "Formato de ID incorrecto"}), 400

    try:
        author = Author.query.get_or_404(id)
        return jsonify(author.to_dict()), 200
    
    except Exception as e:
        return jsonify({"error": "Internal server error", "detalles": str(e)}), 500
