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

@app.get("/stations")
def get_stations():
    return render_template("stations.html.j2", stations=CraftingStation.objects())

@app.post("/item_price/<item_id>")
def set_item_price(item_id):
    print(item_id, request.data.decode(), flush=True)
    try:
        new_price = int(request.data.decode())
    except:
        return "Wrong Format", 400

    item = Item.objects(pk=item_id)
    if not item:
        return
    item=item[0]

    item.average_price = new_price
    item.save()

    return ""

@app.post("/station_tax/<station_id>")
def set_station_tax(station_id):
    print(station_id, request.data.decode(), flush=True)
    try:
        new_tax = int(request.data.decode())
    except:
        return "Wrong Format", 400

    station = CraftingStation.objects(pk=station_id)
    if not station:
        return
    station=station[0]

    station.use_tax = new_tax
    station.save()

    return ""



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