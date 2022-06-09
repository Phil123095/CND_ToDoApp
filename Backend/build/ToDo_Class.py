"""
Creating a to-do item class.
Using the example from the Google documentation as a base: https://firebase.google.com/docs/firestore/query-data/get-data
"""
import datetime
import uuid

class ToDo:
    def __init__(self, title, content, ID=None, created_date=None, due_date=None, tags=[], is_done=False):
        self.ID = ID if ID else str(uuid.uuid4())
        self.title = title
        self.content = content
        self.tags = tags

        if created_date:
            self.created_date = created_date
        else:
            self.created_date = datetime.datetime.now(tz=datetime.timezone.utc)

        self.last_updated = datetime.datetime.now(tz=datetime.timezone.utc)

        self.due_date = due_date
        self.is_done = is_done

    @staticmethod
    def from_dict(source):
        to_do = ToDo(title=source['title'], content=source['content'])

        if 'ID' in source:
            to_do.ID = source['ID']

        if 'created_date' in source:
            to_do.created_date = source['created_date']

        if 'due_date' in source:
            to_do.due_date = source['due_date']

        if 'tags' in source:
            to_do.tags = source['tags']

        if 'is_done' in source:
            to_do.is_done = source['is_done']

        return to_do

    def to_dict(self):
        output = {
            'ID': self.ID,
            'title': self.title,
            'content': self.content
        }

        if self.created_date:
            output['created_date'] = self.created_date

        if self.last_updated:
            output['last_updated'] = self.last_updated

        if self.due_date:
            output['due_date'] = self.due_date

        if self.tags:
            output['tags'] = self.tags

        if self.is_done:
            output['is_done'] = self.is_done

        return output

    def __repr__(self):
        return(
            f'ToDo(\
                ID={self.ID}, \
                title={self.title}, \
                content={self.content}, \
                created_date={self.created_date}, \
                last_updated={self.last_updated}, \
                due_date={self.due_date}, \
                tags={self.tags}\
                is_done={self.is_done}\
            )'
        )