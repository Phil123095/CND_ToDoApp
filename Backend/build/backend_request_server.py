import os
from flask import Flask, request
from google.cloud import firestore
from ToDo_Class import ToDo

app = Flask(__name__)
fs_db = firestore.Client.from_service_account_json('firestore_key.json', strict=False)


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
    fs_db.collection('AllToDo').document(str(ID)).set(todo_item.to_dict())
    print(todo_item)
    return {'ID': ID}


@app.route("/update-todo", methods=["POST"])
def update_todo():
    try:
        todo_request = request.json
        todo_item = ToDo.from_dict(todo_request)
        ID = todo_item.ID
        todo_ref = fs_db.collection('AllToDo').document(str(ID))
        todo_ref.update(todo_item.to_dict())
        return "success"
    except Exception:
        return "failed"


@app.route("/delete-todo", methods=["POST"])
def delete_todo():
    todo_request = request.json
    try:
        todo_ID = todo_request['ID']
    except KeyError:
        return "Please provide the ID of the to-do item for it to be deleted."

    try:
        fs_db.collection('AllToDo').document(todo_ID).delete()
        return "Item successfully deleted"
    except Exception:
        return "Item does not exist"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
