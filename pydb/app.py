from flask import Flask,render_template,request,redirect;
import _mysql_connector;

app = Flask(__name__, template_folder='template')

@app.route("/")
def index(): 
    return render_template("index.html")

if (__name__ == '__main__'):
    app.run(debug=True)