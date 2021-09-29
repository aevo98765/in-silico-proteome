from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from flask_cors import CORS

application = Flask(__name__)
cors = CORS(application, resources={r"/api/*": {"origins": "*"}})
api = Api(application)
from gene_of_interest import poi_proteome, proteome_comparison
from utilities import result_generation, send_mail
class Proteome(Resource):

    def get(self, gene_name, species_id, email):
        subject_string = gene_name + " results"
        proteome = poi_proteome(gene_name, species_id)
        list_in_common = proteome_comparison(proteome, species_id)
        results = result_generation(gene_name, species_id, list_in_common)
        send_mail(email, subject_string, results)

api.add_resource(Proteome, "/<string:gene_name>/<string:species_id>/<string:email>")

if __name__ == "__main__":
    application.run(debug=True)