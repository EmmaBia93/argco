from app.extensions import db
from app.models.book import Book
from app.models.author import Author
from app.models.category import Category
from flask import request, jsonify
from datetime import datetime

def get_all_books():
    
    try:
        books = Book.query.all()
        books_data = [book.to_dict() for book in books]
        return jsonify(books_data), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_book_by_id(id):
    
    try:
        id = int(id)
        
    except ValueError:
        return jsonify({"error": "Formato inválido de Código"}), 400
    
    try:
        book = Book.query.get_or_404(id)
        return jsonify(book.to_dict()), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def create_book():
    try:
        data = request.get_json()
        required_fields = ['isbn', 'title', 'cover', 'synopsis', 'publication_date', 'author_first_name', 'author_last_name', 'category_id']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Faltan campos por introducir: {field}'}), 400

        isbn = data['isbn']
        title = data['title']
        cover = data['cover']
        synopsis = data['synopsis']
        publication_date_str = data['publication_date']
        author_first_name = data['author_first_name']
        author_last_name = data['author_last_name']
        category_id = data['category_id']

       
        try:
            publication_date = datetime.strptime(publication_date_str, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({'error': 'Formato inválido de fecha. Formato válido YYYY-MM-DD.'}), 400

        
        category = Category.query.get(category_id)
        
        if not category:
            return jsonify({'error': 'Category not found'}), 404

        
        author = Author.query.filter_by(first_name=author_first_name, last_name=author_last_name).first()
        
        if not author:
            author = Author(first_name=author_first_name, last_name=author_last_name)
            db.session.add(author)
            db.session.commit()

        
        new_book = Book(
            isbn=isbn,
            title=title,
            cover=cover,
            synopsis=synopsis,
            publication_date=publication_date,
            author_id=author.id,
            category_id=category_id
        )

        
        db.session.add(new_book)
        db.session.commit()

        return jsonify(new_book.to_dict()), 201

    except Exception as e:
       return jsonify({'error': 'Internal server error', 'detalles': str(e)}), 500



def update_book(id):
    
    try:
        
        book = Book.query.get_or_404(id)
        data = request.get_json()

        required_fields = ['isbn', 'title', 'cover', 'synopsis', 'publication_date', 'author_first_name', 'author_last_name', 'category_id']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing field: {field}'}), 400

        isbn = data['isbn']
        title = data['title']
        cover = data['cover']
        synopsis = data['synopsis']
        publication_date_str = data['publication_date']
        author_first_name = data['author_first_name']
        author_last_name = data['author_last_name']
        category_id = data['category_id']

        try:
            publication_date = datetime.strptime(publication_date_str, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({'error': 'Formato inválido de fecha. Formato válido YYYY-MM-DD.'}), 400

        
        category = Category.query.get(category_id)
        if not category:
            return jsonify({f'error': 'La categoria no existe'}), 404

        author = Author.query.filter_by(first_name=author_first_name, last_name=author_last_name).first()
        if not author:
            author = Author(first_name=author_first_name, last_name=author_last_name)
            db.session.add(author)
            db.session.commit()
        
        
        book.isbn = isbn
        book.title = title
        book.cover = cover
        book.synopsis = synopsis
        book.publication_date = publication_date
        book.author_id = author.id
        book.category_id = category_id
        
        
        db.session.commit()

        return jsonify(book.to_dict()), 200

    except Exception as e:
     return jsonify({'error': 'Internal server error', 'detalles': str(e)}), 500



def delete_book(id):
    
    try:
        book = Book.query.get_or_404(id)
        
        db.session.delete(book)
        db.session.commit()
        
        return '', 204
    
    except Exception as e:
       return jsonify({'error': 'Internal server error', 'details': str(e)}), 500
