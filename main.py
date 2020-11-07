import projects #projects definitions are placed in different file
import data

# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template
#create a Flask instance
app = Flask(__name__)

#connects default URL of server to render home.html
@app.route('/')
def home_route():
    return render_template("travel.html", projects=projects.setup())

@app.route("/portfolio/")
def portfolio_route():
    return render_template("portfolio.html", projects=projects.setup())

@app.route("/spain/")
def spain_route():
    return render_template("spain.html", projects=projects.setup())

@app.route("/all/")
def all_route():
    return render_template("all.html", datalist=data.alldata())

@app.route("/england/")
def england_route():
    return "<h1 style='background-color:blue;color:white'>England!</h1>"

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True)