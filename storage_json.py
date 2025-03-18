import json
from istorage import IStorage

class StorageJson(IStorage):
    def __init__(self, filename):
        self.filename = filename
        self._load()

    def _load(self):
        try:
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = []
        self._next_id = max((item['id'] for item in self.data), default=0) + 1

    def _save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=2)

    def list_data(self):
        return self.data

    def add_data(self, author, title, content):
        post = {id: self._next_id, author: author, title: title, content: content}
        self.data.append(post)
        self._next_id += 1
        self._save()
        return post

    def delete_data(self, id, author=None, title=None):
        self.data = [p for p in self.data if p['id'] != id]
        self._save()

    def update_data(self, id, author, title, content):
        for post in self.data:
            if post['id'] == id:
                post.update({author: author, title: title, content: content})
                self._save()
                return post
