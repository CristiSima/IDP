from flask import Flask, render_template, request, redirect
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
        #result[0].isAdmin
        print(str(result[0].isAdmin) + " " + request.headers.get('Referer'), flush=True)
        return redirect(request.headers.get('Referer'))
    
    return redirect("/auth")


if __name__ == '__main__':
    time.sleep(5)
    connect()
    if not len(UserDocument.objects):
        print("DB Empty, Initialising..", flush=True)
        init_users()
        print("Initialisation:\t COMPLETED", flush=True)

    app.run(host="0.0.0.0", debug=False)