from flask import Flask

app = Flask(__name__)

@app.route("/")
def mainpage():
    return "here is the mainpage"

@app.route("/pageuno")
def pageuno():
    return "here is page uno"

@app.route("/pagedos")
def pagedos():
    return "here is page dos"

if __name__ == "__main__":
    app.run()

