from flask import Flask
import trivia_requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    return trivia_requests.send_request(5)


if __name__ == '__main__':
    # in debug mode now
    app.run(debug = True, port = 5000)