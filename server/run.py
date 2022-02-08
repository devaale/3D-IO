import time
from app import create_app, sio
from threading import Lock

lock = Lock()


@sio.on('connect')
def connect():
    print("Connected...")


@sio.on('disconnect')
def disconnect():
    print('Disconnected...')


@sio.on("ping_server")
def receive_message(data):
    with lock:
        count = int(data['count']) * 5
        for i in range(count, count + 5):
            sio.emit('update_count', {'count': i})
            time.sleep(1)


if __name__ == '__main__':
    app = create_app(True)
    sio.run(app)
