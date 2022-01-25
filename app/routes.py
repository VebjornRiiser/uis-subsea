# from crypt import methods
from urllib import request
from flask import render_template, request
import json
from app import app



@app.route('/test')
def test():
    if not "controller_data" in app.config:
        app.config["controller_data"] = "a"
    return json.dumps(app.config["controller_data"])

@app.route('/view')
def view():
    return render_template("view.html")



@app.route('/update_data', methods=["POST"])
def update_data():
    if request.method == 'POST':
        # print("before")
        # print(jsonstr(request.data))
        # print(json.loads(request.data)[0])
        app.config["controller_data"] = json.loads(request.data)
        # print("after")
    return "good"

