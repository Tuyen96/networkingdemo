from flask import Flask
import json

app = Flask(__name__)
post1 = {
    "title" : "Good day",
    "content": "I met a girl."
}
post2 = {
    "title" : "Bad day",
    "content":"Now, I am hungry."
}
print(post1["title"])
print(post1["content"])
posts = [post1, post2]
@app.route('/')
def hello_world():
    return json.dumps(posts)


if __name__ == '__main__':
    app.run()
