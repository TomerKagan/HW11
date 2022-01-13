from flask import Blueprint, render_template
from db import db_access
from flask import request

Update_user = Blueprint('Update_user', __name__, static_folder='static', static_url_path='/Update_user', template_folder='templates')


@Update_user.route('/Update_user', methods=['POST'])
def index():
    username = request.form['username']
    name = request.form['name']
    email = request.form['email']
    query = "UPDATE users SET password = '%s', name='%s',email='%s' WHERE username='%s'" % (password, name, email, username)
    db_access(query=query, query_type='commit')
    return render_template('assignment11.html')
