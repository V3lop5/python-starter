from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)


@app.route('/hello')
def hello():
    name = request.args.get("name", "World")
    app.logger.info(f'Processing hello_word with name {escape(name)}')
    return f'Hello, {escape(name)}!'
