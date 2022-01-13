from flask import Blueprint, render_template
from db import db_access

assignment10 = Blueprint('assignment11', __name__, static_folder='static', static_url_path='/assignment10', template_folder='templates')


@assignment10.route('/assignment10')
def index():
    query = 'select * from users;'
    users = db_access(query=query, query_type='fetch')
    return render_template('assignment10.html', users=users)
