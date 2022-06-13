from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta, timezone
import urllib.request, json, requests
import os


todo = Flask(__name__)
todo.config["SECRET_KEY"] = "group1lovescoding"

@todo.route("/",  methods=["GET","POST"])
def index():
    response = urllib.request.urlopen("https://todoapp-backend-final-7qlre2lo3a-oa.a.run.app/list-all")
    data = response.read()
    dict = json.loads(data)
    return render_template("base.html", todos=dict["list"])

@todo.route("/save", methods=["POST"])
def save():
    if request.method == 'POST':
        title = request.form["title"]
        content = request.form["todo"]
        msg = {'title': title, 'content': content}
        res = requests.post('https://todoapp-backend-final-7qlre2lo3a-oa.a.run.app/create-todo', json=msg)
        return redirect(url_for("index"))

@todo.route("/update/<todo_id>/<title>/<content>", methods=['GET', "POST"])
def update(todo_id, title, content):
    if request.method == 'POST':
        id = todo_id
        title = request.form["title"]
        content = request.form["content"]
        msg = {'ID': id, 'title': title, 'content': content}
        res = requests.post('https://todoapp-backend-final-7qlre2lo3a-oa.a.run.app/update-todo', json=msg)
        return redirect(url_for("index"))
    else:
        return render_template("update.html", todo_id=todo_id, title=title, content=content)

@todo.route("/delete/<todo_id>", methods=['GET', "POST"])
def delete(todo_id):
    #last_updated = datetime.now(timezone.utc) --> when i update the created time also changes
    msg = {'ID': todo_id}
    res = requests.post('https://todoapp-backend-final-7qlre2lo3a-oa.a.run.app/delete-todo', json=msg)
    return redirect(url_for("index"))


if __name__ == '__main__':
    todo.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
