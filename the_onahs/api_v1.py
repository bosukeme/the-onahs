from flask import Blueprint
from flask_restful import Api

from the_onahs.web_pages.views import HomePage, CommentForm

blueprint = Blueprint('api_1_0', __name__)

api = Api(
    blueprint,
    # doc=current_app.config['API_DOCS_URL'],
    catch_all_404s=True
)

api.add_resource(HomePage, "/")
api.add_resource(CommentForm, "/comment")
