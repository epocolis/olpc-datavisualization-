# all the imports

from flask import Flask, make_response ,jsonify
import random
import StringIO

from contextlib import closing
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
         render_template, flash, _app_ctx_stack


# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'


app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('OLPC_SETTINGS', silent=True)


def connect_db():
    pass
    #    return sqlite3.connect(app.config['DATABASE'])


@app.before_request
def before_request():
    pass
    #g.db = connect_db()
    

@app.teardown_request
def teardown_request(exception):
    pass
    """
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
        """


def init_db():
    pass
"""
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
            db.commit()
"""

@app.route('/project_stats', methods=['GET', 'POST'])
def projects_stats_page():
    """ stats about project,location , size mean,max ,age"""
    projects = getAllProjectsFromDB()
    app.logger.debug(dir(projects[0]))
    data = {}
    column_headers = ["Project Name","Country",
                      "Date Started","Number of XO",
                      "Details"] 
    return render_template('project_stats.html',
                           column_headers = column_headers,
                           projects=projects)


@app.route('/applications_stats', methods=['GET', 'POST'])
def applications_stats_page():
    """ stats about application,use, time of day used """
    data = {} 
    return render_template('application_stats.html', data=data)


@app.route('/xo_stats', methods=['GET', 'POST'])
def xo_stats_page():
    """ stats about xo in the wild, version firmware,applications,
    """

    data = {} 
    return render_template('xo_stats.html',data=data )



class Project:
    def create(self, name="Project Name",
               country = "Jamaica",
               dateStarted="Date Started",
               numberOfXO = "1000"): 
        self.name = name
        self.country = country
        self.dateStarted = dateStarted
        self.numberOfXO = numberOfXO

def createDummyProjects(qty):
    projects = []
    for idx in range(1,qty):
        p = Project()
        p.create() 
        projects.append(p)
    return projects    


    

def getAllProjectsFromDB():
    #need to cache this
    #see if new projects have been added to the database
    #if not return the projects in the cache
    projects = createDummyProjects(40)
    return projects

@app.route('/')
def main_page():
    
    return render_template('index.html', page = "FRONT_PAGE")


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))



@app.route('/contact', methods=['GET', 'POST'])
def contact_us():
    error = {} 
    return render_template('contact_us.html', error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)
        

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    init_db()
    app.run()

