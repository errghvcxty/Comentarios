from datetime import datetime

# “banco de dados” em memória
comments = []

class Comment:
    def __init__(self, content, author):
        self.id = len(comments) + 1
        self.content = content
        self.author = author
        self.created_at = datetime.now()
