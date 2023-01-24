from flask import Flask

app = Flask(__name__) # crée une instance de Flask 
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['JSON_AS_ASCII'] = False

from app import route