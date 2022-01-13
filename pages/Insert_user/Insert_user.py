from flask import redirect
from db import db_access
from flask import request
from flask import Blueprint

# Insert_user blueprint definition
Insert_user = Blueprint('Insert_user', __name__, static_folder='static', static_url_path='/Insert_user', template_folder='templates')


# Routes
@Insert_user.route('/Insert_user', methods=['POST'])
def index():
    username = request.form['username']
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    query = "INSERT INTO users(username, name, email, password) values ('%s', '%s','%s','%s')" % (username, name, email, password)
    db_access(query=query, query_type='commit')
    return redirect('/assignment10')
