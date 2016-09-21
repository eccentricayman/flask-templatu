from flask import Flask

app = Flask(__name__)

@app.route("/")
def mainpage():
    return '''
    <h1><b>here is the mainpage</b></h1>
    <br>
    <br>
    <a href="pageuno">here is page uno</a>
    <br>
    <br>
    <a href="pagedos">here is page dos</a>
    <br>
    <br>
    <a href="jklol" style = "font-size: 36px ; background: -webkit-linear-gradient(to left, #00c6ff , #0072ff) ; background: linear-gradient(to left, #00c6ff , #0072ff) ; text-decoration: none ; border 3px solid black ; border-radius: 5px ; padding: 15px; font-family: 'Comic Sans MS' ; color: #FFFFFF">click here 4 something magical</a>'''

@app.route("/pageuno")
def pageuno():
    return '''
    <h1>here is page uno</h1>
    <br>
    <br>
    <a href="/">ew i h8 spanish go bak</a>'''

@app.route("/pagedos")
def pagedos():
    return '''
    <h1>here is page dos</h1>
    <br>
    <br>
    <a href="/">ew i h8 spanish go bak</a>'''

@app.route("/jklol")
def jklol():
    return '''
    <link rel= "stylesheet" type= "text/css" href= "/magic.css">
    <title>500 Internal Server Error</title>
    <h1>Internal Server Error</h1>
    <p>The server encountered an internal error and was unable to complete your request.  Either the server is overloaded or there is an error in the application.</p>
    <br>
    <h2>JK LOL GOT YOU GOOD #MAGICAL</h2>'''

if __name__ == "__main__":
    app.run()

