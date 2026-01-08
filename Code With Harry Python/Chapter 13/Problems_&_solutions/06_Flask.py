from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Padh bhe looh kabhi.....!!!\nReels dekhne se Ghar nahi chalte!</p>"

app.run()