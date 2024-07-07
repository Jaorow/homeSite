from flask import Flask, send_file
import io

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route("/get_all_temps")
def get_all_temps():
    with open('outputs/temps.csv', 'r') as f:
        output = f.read().splitlines()
    return output


if __name__ == "__main__":
    app.run(host='0.0.0.0')
