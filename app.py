import os
from flask import Flask, redirect, request
import logging


logger = logging.getLogger()
app = Flask(__name__)

# Ok, so here's the deal, we have to run our apps off of the
# custom apps host, and app.config['APPLICATION_ROOT'] = os.environ['SCRIPT_NAME']
# just doesn't work at all, so we have to have this until I figure that out.
@app.route(f"{os.environ['SCRIPT_NAME']}/")
def index():
    return 'My Basic Custom App'

# In addition, we need to redirect you to the index route, from
# <host>/apps/<id> to the index at <host>/apps/<id>/
# The reason is that
# The LRS looks at <host>/apps/<id> to determine if the app is working whereas
# DataRobot (when opening the app) redirects you to <basicauth><host>/apps/<id>/
# If you just have <host>/apps/<id> as a route and you land on <basicauth><host>/apps/id/
# then you'll get a 404 then you delete the slash, you won't have the basicauth creds.

@app.before_request
def add_trailing():
    rp = request.path
    if not rp.endswith('/'):
        return redirect(rp + '/')

app.run( host="0.0.0.0", port=8080)
