from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
app = Flask(__name__)
api = Api(app)
from gene_of_interest import poi_proteome, proteome_comparison
import sys
import smtplib, ssl
from email.message import EmailMessage

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# user_put_args = reqparse.RequestParser()
# user_put_args.add_argument("gene", type=str, help="String of gene of interest", required=True)
# user_put_args.add_argument("species_number", type=str, help="Organism id", required=True)



# def abort_if_question_id_doesnt_exist(question_id):
#     if question_id not in questions:
#         abort(404, message="Question id is not valid.")

def send_mail(send_from, send_to, subject, text, file=None, server="localhost"):
    email = "ashevans3000@gmail.com"
    password = "test3000"
    reciever_email = "ashevans3@gmail.com"
    print(email)
    msg=EmailMessage()
    msg['Subject'] = 'AR'
    msg['From'] = email
    msg['To'] = reciever_email
    msg.set_content('Ok it works')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email, password)
        print("Logged in")
        smtp.send_message(msg)
        print("email sent")

def sys_out(gene_choice: str, organism_choice: str, list_in_common: list):
    original_stout = sys.stdout
    file_name: str = gene_choice + "_" + organism_choice
    with open(file_name, "w") as f:
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
        return file_name

class Proteome(Resource):

    def put(self, gene_name, species_id, email):
        # args = user_put_args.parse_args()
        print(gene_name)
        print(species_id)
        print(email)
        proteome = poi_proteome(gene_name, species_id)
        list_in_common = proteome_comparison(proteome, species_id)
        file_name = sys_out(gene_name, species_id, list_in_common)
        send_mail(email, email, "results", "This has worked")



api.add_resource(Proteome, "/<string:gene_name>/<string:species_id>/<string:email>")

if __name__ == "__main__":
    app.run(debug=True)