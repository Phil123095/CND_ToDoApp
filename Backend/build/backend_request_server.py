import os
import dotenv
from flask import Flask, request
from google.cloud import firestore
from ToDo_Class import ToDo

import json
from datetime import datetime, timedelta, timezone

local = True

if local:
    dotenv.load_dotenv()

app = Flask(__name__)

fs_db = firestore.Client.from_service_account_json('cnd-todo-project-9e37f1e232a6.json')


@app.route("/list-all", methods=["GET"])
def list_all_todos():
    all_to_dos = fs_db.collection('AllToDo')
    docs = all_to_dos.stream()

    list_of_todos = [doc.to_dict() for doc in docs]

    for doc in docs:
        todo_item = ToDo.from_dict(doc.to_dict())
        print(todo_item)

    return {'list': list_of_todos}


@app.route("/create-todo", methods=["POST"])
def create_todo():
    todo_request = request.json
    todo_item = ToDo.from_dict(todo_request)
    ID = todo_item.ID
    #todo_request = request.json
    fs_db.collection('AllToDo').document(str(ID)).set(todo_item.to_dict())
    print(todo_item)
    return {'ID': ID}


@app.route("/update-todo", methods=["POST"])
def update_todo():
    todo_request = request.json
    todo_item = ToDo.from_dict(todo_request)
    ID = todo_item.ID
    todo_ref = fs_db.collection('AllToDo').document(str(ID))
    todo_ref.update(todo_item.to_dict())
    return


@app.route("/delete-todo", methods=["POST"])
def delete_todo():
    todo_request = request.json
    todo_ID = todo_request['ID']
    fs_db.collection('AllToDo').document(todo_ID).delete()
    return


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))