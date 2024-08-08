from flask import Flask, render_template

app = Flask(__name__);

@app.route("/")
def do_it():
    return render_template('got_js.html')

