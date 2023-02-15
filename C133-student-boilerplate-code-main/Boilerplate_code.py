#Importing flask module in the project
from flask import Flask

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/")

#‘/’ URL is bound with first_flask function.
def first_flask():

    return "This is my first flask program"

#run the application on local server
app.run()

@app.route("/flask2")

def second_flask():
    
    return "Pass any message"

app.run(debug = True)

@app.route("/index")

def web_page():
    
    return render_template("index.html")

app.run(debug = True)





    
    
