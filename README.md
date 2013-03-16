Flask-Pigeon
============

- Flask Messages Framework
- A simple Flask extension implements the similar function as Django's messages framework.
- Example included, but very bind to Bootstrap.

Examples
============

app.py
------------

```python
from flask import Flask, render_template
from flask.ext import pigeon
app = Flask("APP")
pigeon = pigeon.Pigeon(app)


@app.route("/")
def index():
    pigeon.info("Hello")
    pigeon.error("Hello")
    pigeon.success("Hello")
    pigeon.warning("Hello")
    return render_template("home.html")
```

_message.html
-------------
```html
<div class="span6">
    {% if messages %}
    {% for message in messages %}
    <div class="alert {{ message.tag }}">
        <button type="button" class="close" data-dismiss="alert">&times;</button>
        <h2>{{ message.message }}</h2>
        See?
    </div>
    {% endfor %}
    {% else %}
    <h1>Hello World!</h1>
    {% endif %}
</div>
```

home.html
-------------
```html
<!doctype html>
	<head>
		<script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
		<link href="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/css/bootstrap-combined.min.css" rel="stylesheet">
		<title>Hello from Flask</title>
	</head>
	<body>
		<div class="container">
		{% include "_message.html" %}
		</div>
		<script src="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/js/bootstrap.min.js"></script>
	</body>
</html>
```
