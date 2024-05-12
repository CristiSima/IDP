from flask import Flask, render_template, request, session, redirect
from documents import *
from init_db import init_db
from functools import wraps
import mongoengine
import time

def is_authenticated():
    return session.get("username") != None

def authentication_required(func):

    @wraps(func)
    def temp(*argv, **kwargs):
        if is_authenticated():
            return func(*argv, **kwargs)

        return redirect("/auth")

    return temp

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
        "is_authenticated": is_authenticated,
    }

@app.get("/items")
def get_items():
    return render_template("items.html.j2", items=Item.objects())

@app.get("/stations")
def get_stations():
    return render_template("stations.html.j2", stations=CraftingStation.objects())

@app.get("/recipe/<recipe_id>")
def recipeinfo(recipe_id):
    recipe = Recipe.objects(pk=recipe_id)
    if len(recipe) != 1:
        return "", 404
    recipe: Recipe = recipe[0]

    return render_template("recipe.html.j2",
        recipe=recipe,
    )

@app.get("/item/<item_id>")
def iteminfo(item_id):
    item = Item.objects(pk=item_id)
    if not item:
        return
    item: Item=item[0]

    item.recipes_using()

    return render_template("item.html.j2",
        item=item,
        recipes_for=item.recipes_for(),
        recipes_using=item.recipes_using(),
        # made_by_rows=cur.callfunc("get_recipes_for_item", oracledb.DB_TYPE_CURSOR, [item_id,]),
        # used_in_rows=cur.callfunc("get_recipes_using_item", oracledb.DB_TYPE_CURSOR, [item_id,]),
    )

@app.post("/item_price/<item_id>")
@authentication_required
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
@authentication_required
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
    app.secret_key = "0f98b8ae9bf345c9123734997222404a67929b27e6724d5651305138135893bb"
    time.sleep(5)
    connect()
    if not len(Item.objects):
        print("DB Empty, Initialising..", flush=True)
        init_db()
        print("Initialisation:\t COMPLETED", flush=True)

    app.run(host="0.0.0.0", debug=False)