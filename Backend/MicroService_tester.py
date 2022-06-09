import requests
import json

def request_to_backend(url_to_request, request_content=None):
    if request_content:
        response = requests.post(url_to_request, json=request_content)
    else:
        response = requests.get(url_to_request)

    content = json.loads(response.text)

    return content


def list_all_todos(base_url):
    endpoint = '/list-all'
    list_of_todos = request_to_backend(url_to_request=base_url + endpoint)

    return list_of_todos


def create_todo(base_url, todo_request):
    endpoint = '/create-todo'
    out_ID = request_to_backend(url_to_request=base_url + endpoint, request_content=todo_request)
    return out_ID


def update_todo(base_url, todo_request):
    endpoint = '/update-todo'
    out_ID = request_to_backend(url_to_request=base_url + endpoint, request_content=todo_request)
    return out_ID


def delete_todo(base_url, todo_ID):
    endpoint = '/delete-todo'
    out_ID = request_to_backend(url_to_request=base_url + endpoint, request_content={'ID': todo_ID})
    return out_ID



if __name__ == '__main__':
    base_url = "https://todoapp-backend-final-7qlre2lo3a-oa.a.run.app"

    todo_list = [
        {
            'title': 'Go home',
            'content': "I really don't feel like it, but I need to...."
        },
        {
            'title': 'Drinks with friends',
            'content': "Go to the gym plssss...."
        },
        {
            'title': 'Study for exam',
            'content': "Hey there",
            'is_done': True
        }
    ]

    #for element in todo_list:
    #    print(create_todo(base_url=base_url, todo_request=element))

    print(list_all_todos(base_url=base_url))

