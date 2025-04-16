from flask import Blueprint, request, jsonify
import sqlite3

schedule_bp = Blueprint('schedule', __name__)

# ✅ 일정 등록 API (POST)

@schedule_bp.route('/schedules', methods=['POST'])
def add_schedule():
    data = request.get_json()
    title = data.get('title')
    time = data.get('time')

    if not title or not time:
        return jsonify({"error": "title과 time은 필수입니다"}), 400

    conn = sqlite3.connect('schedule.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO schedules (title, time, user_id) VALUES (?, ?, ?)", (title, time, 1))  # 일단 user_id는 1로 고정
    conn.commit()
    conn.close()

    return jsonify({"message": "일정이 성공적으로 등록되었습니다!"}), 201


# ✅ 일정 목록 조회 API (GET)

@schedule_bp.route('/schedules', methods=['GET'])
def get_schedules():
    conn = sqlite3.connect('schedule.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, time FROM schedules")
    rows = cursor.fetchall()
    conn.close()

    schedules = []
    for row in rows:
        schedules.append({
            "id": row[0],
            "title": row[1],
            "time": row[2]
        })

    return jsonify(schedules)
