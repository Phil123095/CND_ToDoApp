from flask import Flask, render_template, request, redirect, url_for
import urllib.request
import json
import requests
import os
import google.auth.transport.requests as google_tp
import google.oauth2.id_token as google_id_token


todo = Flask(__name__)
todo.config["SECRET_KEY"] = "group1lovescoding"
audience = "https://todoapp-backend-final-7qlre2lo3a-oa.a.run.app/"


@todo.route("/",  methods=["GET","POST"])
def index():
    req = urllib.request.Request("https://todoapp-backend-final-7qlre2lo3a-oa.a.run.app/list-all")
    auth_req = google_tp.Request()
    id_token = google_id_token.fetch_id_token(auth_req, audience)
    req.add_header("Authorization", f"Bearer {id_token}")
    response = urllib.request.urlopen(req)
    data = response.read()
    dict = json.loads(data)
    return render_template("base.html", todos=dict["list"])


@todo.route("/save", methods=["POST"])
def save():
    if request.method == 'POST':
        title = request.form["title"]
        content = request.form["todo"]
        msg = {'title': title, 'content': content}
        auth_req = google_tp.Request()
        id_token = google_id_token.fetch_id_token(auth_req, audience)
        res = requests.post('https://todoapp-backend-final-7qlre2lo3a-oa.a.run.app/create-todo', json=msg, headers={"Authorization": f"Bearer {id_token}"})
        return redirect(url_for("index"))


@todo.route("/update/<todo_id>/<title>/<content>", methods=['GET', "POST"])
def update(todo_id, title, content):
    if request.method == 'POST':
        id = todo_id
        title = request.form["title"]
        content = request.form["content"]
        msg = {'ID': id, 'title': title, 'content': content}
        auth_req = google_tp.Request()
        id_token = google_id_token.fetch_id_token(auth_req, audience)
        res = requests.post('https://todoapp-backend-final-7qlre2lo3a-oa.a.run.app/update-todo', json=msg, headers={"Authorization": f"Bearer {id_token}"})
        return redirect(url_for("index"))
    else:
        return render_template("update.html", todo_id=todo_id, title=title, content=content)


@todo.route("/delete/<todo_id>", methods=['GET', "POST"])
def delete(todo_id):
    # last_updated = datetime.now(timezone.utc) --> when i update the created time also changes
    msg = {'ID': todo_id}
    auth_req = google_tp.Request()
    id_token = google_id_token.fetch_id_token(auth_req, audience)
    res = requests.post('https://todoapp-backend-final-7qlre2lo3a-oa.a.run.app/delete-todo', json=msg, headers={"Authorization": f"Bearer {id_token}"})
    return redirect(url_for("index"))


if __name__ == '__main__':
    todo.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
