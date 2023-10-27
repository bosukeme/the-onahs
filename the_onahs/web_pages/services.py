from datetime import datetime
from the_onahs.mongo_util import Comments


class Comment:
    def __init__(self, name, comment, email) -> None:
        self.name = name
        self.email = email
        self.comment = comment

    def upload_comment(self):
        query = {"email": self.email}
        data = {
            "name": self.name,
            "email": self.email,
            "comment": self.comment,
            "comment_date": str(datetime.now())
        }
        Comments.update_record(query=query, data=data)

    @classmethod
    def get_comments(cls):
        comments = Comments.get_records(query={})

        return comments


def send_comment_func(name, email, message):

    Comment(name=name, email=email, comment=message).upload_comment()
