from flask import Flask, request, jsonify, make_response
from flask_restx import Api, Resource, fields
import joblib
import numpy as np
import sys

flask_app = Flask(__name__)
app = Api(app=flask_app,
          version="1.0",
          title="Penguin identifier",
          description="Predict the type of penguin")

name_space = app.namespace('prediction', description='Prediction APIs')

model = app.model('Prediction params',
                  {'island': fields.Float(required=True,
                                          description="island",
                                          help="island cannot be blank"),
                   'bill_length_mm': fields.Float(required=True,
                                                  description="bill_length_mm",
                                                  help="bill_length_mm cannot be blank"),
                   'bill_depth_mm': fields.Float(required=True,
                                                 description="bill_depth_mm",
                                                 help="bill_depth_mm cannot be blank"),
                   'flipper_length_mm': fields.Float(required=True,
                                                     description="flipper_length_mm",
                                                     help="flipper_length_mm cannot be blank"),
                   'body_mass_g': fields.Float(required=True,
                                               description="body_mass_g",
                                               help="body_mass_g cannot be blank"),
                   'sex': fields.Float(required=True,
                                       description="sex",
                                       help="sex cannot be blank")})

classifier = joblib.load('classifier.joblib')


@ name_space.route("/")
class MainClass(Resource):

    def options(self):
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add('Access-Control-Allow-Headers', "*")
        response.headers.add('Access-Control-Allow-Methods', "*")
        return response

    @ app.expect(model)
    def post(self):
        try:
            formData = request.json
            data = [val for val in formData.values()]
            prediction = classifier.predict(np.array(data).reshape(1, -1))
            types = {0: "Adelie",
                     1: "Chinstrap", 2: "Gentoo"}
            response = jsonify({
                "statusCode": 200,
                "status": "Prediction made",
                "result": "The type of penguin is: " + types[prediction[0]]
            })
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        except Exception as error:
            return jsonify({
                "statusCode": 500,
                "status": "Could not make prediction",
                "error": str(error)
            })
