from flask import Flask, render_template, request, redirect, session, jsonify
import uuid

from init_users import init_users
from user_docs import *
import time

app = Flask(__name__)


@app.get('/')
def hello():
    return render_template('index.html')

@app.post("/")
def login():
    username = request.form.getlist("username")[0]
    passw = request.form.getlist("password")[0]
    hash = makePassHash(passw)
    result = UserDocument.objects.filter(username=username, passw=hash)
    if len(result) != 0:
        session['username'] = username
        #todo: properly redirect
        return redirect(request.headers.get('Referer'))
    
    return redirect("/auth")


if __name__ == '__main__':
    #todo: move this
    app.secret_key = "0f98b8ae9bf345c9123734997222404a67929b27e6724d5651305138135893bb"
    time.sleep(5)
    connect()
    if not len(UserDocument.objects):
        print("DB Empty, Initialising..", flush=True)
        init_users()
        print("Initialisation:\t COMPLETED", flush=True)

    app.run(host="0.0.0.0", debug=False)