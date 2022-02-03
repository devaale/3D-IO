import time
from app import create_app, sio
from threading import Lock

message_lock = Lock()


@sio.on('connect')
def connect():
    print("Connected...")


@sio.on('disconnect')
def disconnect():
    print('Disconnected...')


@sio.on("message")
def receive_message(data):
    with message_lock:
        print(data)
        for i in range(int(data['count']) * 5, int(data['count']) * 5 + 5):
            sio.emit('message', {'count': i})
            time.sleep(1)


if __name__ == '__main__':
    app = create_app(True)
    sio.run(app)
