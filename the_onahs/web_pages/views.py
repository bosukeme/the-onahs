from flask_restful import Resource
from flask import request, Response, render_template
from the_onahs.dramatiq_actor.send_comment import send_comment_dramatiq
from .services import Comment


class HomePage(Resource):
    def get(self):

        comments = list(Comment.get_comments())

        comments_count = len(comments)

        return Response(response=render_template("Page-2.html",
                                                 comments_count=comments_count,
                                                 comments=comments))


class CommentForm(Resource):
    def post(self):

        data = request.form

        message = data['message']
        name = data['name']
        email = data['email']

        send_comment_dramatiq.send(name, email, message)

        return {"success": True}
