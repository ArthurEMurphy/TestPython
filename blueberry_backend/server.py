import json
from flask import Flask
from about_me import me
from mock_data import catalog #IMPORTANT STEP

app = Flask('blueberry')


@app.route("/", methods=['GET'])  # root
def home():
    return "This is the home page"

# Create an about endpoint and show


@app.route("/about")
def about():
    return f"{me['first']} {me['last']}"  # return me["first"] + " " + ["last"]


@app.route("/myaddress")
def address():
    return f'  {me["address"]["number"]} {me["address"]["street"]}'


# JSON - JaveScript Object Notation
############################################################################################# API ENDPOINTS ##################################################################################################

@app.route("/api/catalog", methods=["GET"])
def get_catalog():
    return json.dumps(catalog)



app.run(debug=True)
