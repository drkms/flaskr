from flask import Flask

app = Flask(__name__, instance_relative_config=True)

from app import views

app.config.from_object('config')

from flask.ext.login import LoginManager
#from flask.ext.acl import ACLManager

authn = LoginManager(app)
authn.init_app(app)

#authz = ACLManager(app)

