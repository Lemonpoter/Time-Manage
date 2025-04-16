from flask import Flask
from routes.schedule_routes import schedule_bp  # 👈 이 줄 추가
from routes.user_routes import user_bp

app = Flask(__name__)

app.register_blueprint(schedule_bp)  # 👈 이 줄 추가
app.register_blueprint(user_bp)

@app.route('/')
def home():
    return "안녕하세요! Flask 서버가 잘 작동 중입니다 😊"

if __name__ == '__main__':
    app.run(debug=True)
