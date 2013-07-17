# all the imports
import os
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore, \
        UserMixin, RoleMixin, login_required
from flask.ext.security.utils import encrypt_password
from flask.ext.security.views import register


# configuration
DEBUG = True

app = Flask(__name__)
app.config['SECURITY_REGISTERABLE'] = True
app.config["SECURITY_PASSWORD_HASH"] = "bcrypt"
app.config["SECURITY_PASSWORD_SALT"] = "salty"
app.secret_key = 'D\xf04\xa9\xa8\xac`\x99?\x98m\xd7\x98j\x89\xac6\x84&\x87\xe4y\xce\xceKl\xd0E`D\xa0\n' 
app.config.from_object(__name__)
app.config.from_envvar('OLPC_SETTINGS', silent=True)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL","postgresql://olpc:!hessian!@localhost/olpc_dashboard")
db = SQLAlchemy(app)


# Define models
roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Create a user to test with
"""
@app.before_first_request
def create_user():
    db.create_all()
    user_datastore.create_user(email='leotisbuchanan2@gmail.com',password=encrypt_password('password'))
    db.session.commit()
"""


@app.teardown_request
def teardown_request(exception):
    pass


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


@app.route('/applications_stats', methods=['GET'])
def applications_stats_page():
    """ stats about application,use, time of day used """
    data = {} 
    return render_template('application_stats.html', data=data)


@app.route('/register', methods=['GET'])
def register_wrapper():
    return register()


@app.route('/about_us', methods=['GET'])
def about_us():
    return "about us"


@app.route('/xo_stats', methods=['GET'])
def xo_stats_page():
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
@login_required
def main_page():
      return render_template('index.html', page = "FRONT_PAGE")


@app.route('/contact', methods=['GET', 'POST'])
def contact_us():
    error = {} 
    return render_template('contact_us.html', error=error)




if __name__ == '__main__':
    app.run()

