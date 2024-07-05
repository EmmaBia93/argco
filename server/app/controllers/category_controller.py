from app.extensions import db
from app.models.category import Category
from flask import request, jsonify

def get_all_categories():
    try:
        categories = Category.query.all()
        categories_data = [category.to_dict() for category in categories]

        return jsonify(categories_data), 200
    
    except Exception as e:
       return jsonify({"error": "Internal server error", "detalles": str(e)}), 500

def get_category_by_id(id):
    try:
        id = int(id)
    except ValueError:
        return jsonify({"error": "Formato de ID incorrecto"}), 400

    try:
        category = Category.query.get_or_404(id)
        return jsonify(category.to_dict()), 200
    except Exception as e:
       return jsonify({"error": "Internal server error", "detalles": str(e)}), 500