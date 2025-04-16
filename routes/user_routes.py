from flask import Blueprint, request, jsonify
import sqlite3

user_bp = Blueprint('user', __name__)

# ✅ 회원가입
@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "username과 password는 필수입니다"}), 400

    conn = sqlite3.connect('schedule.db')
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
    except sqlite3.IntegrityError:
        return jsonify({"error": "이미 존재하는 사용자입니다"}), 409
    finally:
        conn.close()

    return jsonify({"message": "회원가입 성공!"}), 201

# ✅ 로그인
@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    conn = sqlite3.connect('schedule.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({"message": "로그인 성공!"})
    else:
        return jsonify({"error": "아이디 또는 비밀번호가 일치하지 않습니다"}), 401
