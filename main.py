from flask import Flask
from api import api

app = Flask('my web app')
app.register_blueprint(api)


app.run()