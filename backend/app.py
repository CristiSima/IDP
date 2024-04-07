from flask import Flask, render_template, request, Blueprint
from documents import *
from init_db import init_db
import mongoengine
import time

app = Flask(__name__)

@app.context_processor
def renderers():
    return {
        "round": round,
        "zip": zip,
        "list": list,
        "enumerate": enumerate,
        "print": print,
        "len": len,
    }

@app.get("/items")
def get_items():
    return render_template("items.html.j2", items=Item.objects())


@app.get("/")
def test():
    return render_template("home.html.j2")


if __name__ == '__main__':
    time.sleep(5)
    connect()
    if not len(Item.objects):
        print("DB Empty, Initialising..", flush=True)
        init_db()
        print("Initialisation:\t COMPLETED", flush=True)

    app.run(host="0.0.0.0", debug=False)