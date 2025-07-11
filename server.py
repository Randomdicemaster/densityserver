from flask import Flask, request
from flask_socketio import SocketIO
import eventlet

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# REST API로 값 수신 (측정 프로그램에서 보냄)
@app.route('/update', methods=['POST'])
def update():
    data = request.json
    value = data.get("density")
    if value is not None:
        print(f"측정값 수신: {value}")
        socketio.emit('new_density', {'density': value})
    return '', 200

# 웹소켓 연결 테스트
@socketio.on('connect')
def handle_connect():
    print("웹 클라이언트 접속됨")

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5000)
