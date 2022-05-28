import json
from flask import Flask
from about_me import me
from mock_data import catalog  # IMPORTANT STEP

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
# Postman -> Test endpoints of REST APIs

@app.route("/api/catalog", methods=["GET"])
def get_catalog():
    return json.dumps(catalog)


@app.route("/api/catalog/count", methods=["GET"])
def get_count():
    # Here... count how many products are in the list catalog
    counts = len(catalog)

    return json.dumps(counts)  # return the value

# Request 127.0.0.1:5000/api/product/5f40a6baac77a903d8f682c6


@app.route("/api/product/<id>", methods=["GET"])
def get_product(id):
    # cheapest =

    return json.dumps(id)

# @app.route("/api/total/<id>", methods=["GET"])
# def get_total():
    # total =

    # return json.dumps(total)


app.run(debug=True)
