from flask import Flask
import json

app = Flask(__name__)
post1 = {
    "title" : "Good day",
    "content": "I met a girl."
}


@app.route('/')
def hello_world():
    return json.dumps(post1)


if __name__ == '__main__':
    app.run()
