class Todo:
    def __init__(self, code_id: int, title: str, description: str):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []
    def mark_completed(self):
       self.completed = True

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        return f"{self.code_id} - {self.title}"

class TodoBook:
    def __init__(self):
        self.todos = dict[int: Todo]

    def add_todo(self, object):
        self.title: str = "Hola"
        self.description: str = "Como"
        code_id = len(self.todos) + 1
        self.object = object

        self.object = Todo(self.code_id, self.title, self.description)
        self.todos = dict[self.code_id, self.object]

        return code_id

    def pending_books(self):









