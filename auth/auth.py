from flask import Flask, render_template
import time

app = Flask(__name__)


@app.get('/')
def hello():
    return render_template('index.html')

@app.post("/")
def login():
    # ImmutableMultiDict([('username', 'asd'), ('password', 'asd')])
    print(request.form, flush=True)
    return redirect("/auth")


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)