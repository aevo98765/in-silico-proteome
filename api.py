from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
app = Flask(__name__)
api = Api(app)
from gene_of_interest import poi_proteome, proteome_comparison
import sys


# user_put_args = reqparse.RequestParser()
# user_put_args.add_argument("gene", type=str, help="String of gene of interest", required=True)
# user_put_args.add_argument("species_number", type=str, help="Organism id", required=True)



# def abort_if_question_id_doesnt_exist(question_id):
#     if question_id not in questions:
#         abort(404, message="Question id is not valid.")

def sys_out(gene_choice: str, organism_choice: str, list_in_common: list):
    original_stout = sys.stdout
    with open(gene_choice + "_" + organism_choice, "w") as f:
        sys.stdout = f
        print("1. Gene name.")
        print("2. Number of proteome hits in common.")
        print("3. Proteome hits in common relative to the proteome size.")
        print("4. A list of the proteome hits in common.")
        print("\n")
        print("---------------")
        print("\n")

        index = 0
        for gene in list_in_common:
            index += 1
            print(str(index) + ".", end=" ")
            for e in gene:
                print(e)
            print("\n")
            print("---------------")
            print("\n")
        sys.stdout = original_stout
        print("Complete! Check the files.")

class Proteome(Resource):

    def put(self, gene_name, species_id):
        # args = user_put_args.parse_args()
        print(gene_name)
        print(species_id)
        proteome = poi_proteome(gene_name, species_id)
        list_in_common = proteome_comparison(proteome, species_id)
        sys_out(gene_name, species_id, list_in_common)



api.add_resource(Proteome, "/<string:gene_name>/<string:species_id>")

if __name__ == "__main__":
    app.run(debug=True)