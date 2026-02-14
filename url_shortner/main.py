from flask import Flask, jsonify, request, redirect
import sqlite3
import string
import random


app = Flask(__name__)
DB_NAME = 'urls.db'

# ================= DATABASE =================
def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
                     CREATE TABLE IF NOT EXISTS urls(
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                         original_url TEXT NOT NULL,
                         short_code TEXT NOT NULL UNIQUE
                     )
                     """)
        conn.commit()
        
def generate_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def save_url(original_url):
    short_code = generate_code()
    
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("INSERT INTO urls (original_url, short_code) VALUES (?, ? )", (original_url, short_code))
        conn.commit()
        
        return short_code
    
def get_original_url(short_code):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute("SELECT original_url FROM urls WHERE short_code = ?", (short_code,)) 
        row = cursor.fetchone()
        
        return row[0] if row else None
    
# ================= ROUTES =================
@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get('url')
    if not original_url:
        return jsonify({"short_url": None, "error": "No URL provided"}), 400
    
    code = save_url(original_url)  
    return jsonify({"short_url": request.host_url + code}), 201

@app.route('/<short_code>', methods=["GET"])
def redirect_url(short_code):
    original_url = get_original_url(short_code)
    
    if not original_url:
        return jsonify({"error": "URL not found"}), 404
    
    return redirect(original_url)

# ================= MAIN =================
if __name__ == '__main__':
    init_db()
    app.run(debug=True)