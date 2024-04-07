from flask import Flask, render_template, request, Blueprint
from documents import *
import mongoengine
import time

app = Flask(__name__)


@app.get("/")
def test():
    return ""

if __name__ == '__main__':
    time.sleep(5)
    connect()
    if not len(Item.objects):
        print("DB Empty, Initialising..", flush=True)
        init_db()
        print("Initialisation:\t COMPLETED", flush=True)
        
    app.run(host="0.0.0.0", debug=False)