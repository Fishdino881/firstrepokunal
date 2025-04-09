# app.py
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"
    

@app.route("/pooja")
def hello_world_fancy():
    greetings = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Sister</title>
</head>
<body>

    <h1>My Sister</h1>

    <h2>Who is My Sister?</h2>
    <p>My sister is my best friend and my greatest support. She is always there for me in both good times and bad. She brings joy and laughter into my life every day.</p>

    <h2>Why I Love My Sister</h2>
    <p>She is kind, caring, and understanding. No matter what happens, she always knows how to make me smile. Her love and support mean the world to me.</p>

    <h2>Memories with My Sister</h2>
    <p>Some of my best childhood memories are with my sister. Whether we were playing together, having fun, or even fighting, every moment was special.</p>

    <h2>What Makes Her Special?</h2>
    <p>My sister is unique because of her ability to make everyone around her feel loved and cared for. Her strength, wisdom, and loving nature inspire me every day.</p>

</body>
</html>


    """
    return greetings
