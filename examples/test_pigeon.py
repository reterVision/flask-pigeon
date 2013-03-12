from flask import Flask, render_template
from flask.ext import pigeon
app = Flask("APP")
pigeon = pigeon.Pigeon(app)


@app.route("/")
def index():
    pigeon.info("Hello")
    pigeon.error("Hello")
    pigeon.success("Hello")
    pigeon.warning("HellO")
    return render_template("home.html")


@app.route("/world")
def other():
    pigeon.info("World")
    return render_template("world.html")


if __name__ == "__main__":
    app.run(port=5002, debug=True)
