from flask import request, json, Response, Blueprint

jobs_api = Blueprint('jobs', __name__)

@jobs_api.route('/', methods=['GET'])
def jobs_test():
    return f'Jobs index page'