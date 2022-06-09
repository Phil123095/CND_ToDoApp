# CND_ToDoApp
Experimenting with Google Cloud Run (Group 3: Coco Koban, Philippe Henderson, Julius Von Davier, Nicolò Prini, Nora Tombers)

### Backend
- Flask-based API microservice. 
- Endpoint: https://todoapp-backend-final-7qlre2lo3a-oa.a.run.app

- What it does: Can write, update, delete and read all to-do items to and from a Firestore DB.
- What data it receives: object-format (a dict) data.
- Actions:
  - **/list-all** --> Returns all todo list items in the firestore DB as a list.
    - Inputs: None
    - Action: Retrieves all the documents in the Firestore DB 'AllToDo' collection.
    - Returns: A nice list of todo objects.
  - **/create-todo** --> Creates a todo list item, returns the ID of the created item. 
    - Inputs: To-do object (dictionary), with **at minimum**: {'title': :your title:, 'content': :your content:}
    - Action: Creates new document in Firestore DB 'AllToDo' collection, and writes the data to the document.
    - Returns: Unique ID for the todo item.
  - **/update-todo** --> Update an existing todo list item. 
    - Inputs: To-do object (dictionary), with **at minimum**: The fields you wish to change (e.g. Title, is_done, etc.) AND the current ID of the todo item.
    - Action: Retrieves the document in the Firestore collection based on its ID, and modifies the desired fields. 
    - Returns: success or fail message. 
  - **/delete-todo** --> Delete an existing todo list item.
    - Inputs: To-do item ID, in the form of {'ID': :to-do-ID:}.
    - Action: Deletes the document in Firestore that corresponds to that ID. 
    - Returns: success or fail message.

Sources:
- [Deploying a Python Service to Cloud Run](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service)
- [Firestore Documentation](https://firebase.google.com/docs/firestore)
- [GCloud Firestore Data Models](https://firebase.google.com/docs/firestore/data-model) <-- The explainer videos are really good.

Remaining To Do:
- Clean up backend code to handle errors better. 
- Build CI/CD pipeline
- Verify that how we're connecting to Firestore is the right way. Need to double-check with the Qwiklabs.
- Look into scalability parameters and all that stuff.
