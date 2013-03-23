from flask import Flask, render_template, request
from flask.ext import pigeon
app = Flask("APP")
pigeon = pigeon.Pigeon(app)


@app.route("/")
def index():
    pigeon.info(request, "Hello")
    pigeon.error(request, "Hello")
    pigeon.success(request, "Hello")
    pigeon.warning(request, "HellO")
    return render_template("home.html")


@app.route("/world")
def other():
    pigeon.info(request, "World")
    return render_template("world.html")


if __name__ == "__main__":
    app.run(port=5002, debug=True)
