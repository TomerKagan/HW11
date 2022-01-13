from flask import redirect
from flask import Blueprint
from db import db_access
from flask import request

Delete_user = Blueprint('Delete_user', __name__, static_folder='static', static_url_path='/Delete_user', template_folder='templates')


@Delete_user.route('/Delete_user', methods=['POST'])
def index():
    username = request.form['username']
    query = "DELETE FROM  users WHERE username='%s';" % username
    db_access(query=query, query_type='commit')
    return redirect('/assignment10', messeage=True)


