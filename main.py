from flask import Flask, send_file
import io

app = Flask(__name__)


def get_temps_from_file():
    with open('outputs/temps.csv', 'r') as f:
        output = f.read().splitlines()
    output.reverse()
    return output

@app.route("/")
def hello():
    o = get_temps_from_file()
    line = o[0].split(', ')
    return f""" <h1>7/25 Lloyd ave</h1>
                <p>{line[1]}°, {line[2]}%</p> 
                <a href='/get_all_temps'>history</a>
            """

@app.route("/get_all_temps")
def get_all_temps():
    output = get_temps_from_file()
    o = "<a href='/'>Home</a>"
    for line in output:
        line = line.split(', ')
        o += f"<p>{line[0]} --> {line[1]}°, {line[2]}%</p>"
    return o


if __name__ == "__main__":
    app.run(host='0.0.0.0')
