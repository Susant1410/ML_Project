from flask import Flask
import sys
from housing.logger import logging
from housing.exception import HousingException
app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("Error message")
    except Exception as e:
            housing = HousingException(e,sys)
            logging.info("Housing Error Message")
            logging.info("Test the project")
    return "My First ML Projct"

if __name__=="__main__":
    app.run(debug=True)