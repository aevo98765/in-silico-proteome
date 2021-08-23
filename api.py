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
from email.mime.application import MIMEApplication
from os.path import basename




# user_put_args = reqparse.RequestParser()
# user_put_args.add_argument("gene", type=str, help="String of gene of interest", required=True)
# user_put_args.add_argument("species_number", type=str, help="Organism id", required=True)



# def abort_if_question_id_doesnt_exist(question_id):
#     if question_id not in questions:
#         abort(404, message="Question id is not valid.")

def send_mail(send_to, subject, text, file_name=None, server="localhost"):
    email = "ashevans3000@gmail.com"
    password = "test3000"
    reciever_email = "ashevans3@gmail.com"
    print(email)
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = reciever_email
    msg.set_content(text)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email, password)
        print("Logged in")
        smtp.send_message(msg)
        print("email sent")

def sys_out(gene_choice: str, organism_choice: str, list_in_common: list):
    results = """
    1. Gene name.\n
    2. Number of proteome hits in common.\n
    3. Proteome hits in common relative to the proteome size.\n
    4. A list of the proteome hits in common.\n
    \n
    ---------------
    \n
    """
    print(list_in_common)
    index = 0
    for gene in list_in_common:
        index += 1
        print(index)
        results += str(index) + "."
        for e in gene:
            results += (str(e) + ",\n")
        results += "\n"
        results += "---------------"
        results += "\n"
    print(results)
    print("Complete!")
    return results

class Proteome(Resource):

    def put(self, gene_name, species_id, email):
        # args = user_put_args.parse_args()
        print(gene_name)
        print(species_id)
        print(email)
        subject_string = gene_name + " results"
        proteome = poi_proteome(gene_name, species_id)
        list_in_common = proteome_comparison(proteome, species_id)
        results = sys_out(gene_name, species_id, list_in_common)
        send_mail(email, subject_string, results)



api.add_resource(Proteome, "/<string:gene_name>/<string:species_id>/<string:email>")

if __name__ == "__main__":
    app.run(debug=True)