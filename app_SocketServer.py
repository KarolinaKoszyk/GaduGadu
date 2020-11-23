from flask import Flask
from flask_classful import FlaskView,route
from GaduGaduServer import GaduGaduServerView
ggServer = GaduGaduServerView()
app = Flask("GaduGadu")
ggServer.register(app)
print ("Enter exit to close server!")
#    server.CheckForNewClient()
app.run(debug=True)

