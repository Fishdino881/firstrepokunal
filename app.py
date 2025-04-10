from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def homepage():
    return send_file('codm.html')

if __name__ == '__main__':
    app.run(debug=True)
