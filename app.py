from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dKbYCeneRs'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('cts_msg')
def msg_received(data):
    emit('stc_msg', {'data': data['msg']})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
