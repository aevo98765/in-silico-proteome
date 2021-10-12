import smtplib
import boto3
from botocore.exceptions import ClientError
from email.message import EmailMessage


def send_mail(send_to, subject, text):
    SENDER = "ashevans3000@gmail.com"
    RECIPIENT = send_to
    AWS_REGION = "eu-west-2"
    SUBJECT = subject
    BODY_TEXT = text
    CHARSET = "UTF-8"

    client = boto3.client('ses', region_name = AWS_REGION)

    try:
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT
                ],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:")
        print(response['MessageId'])


    # msg = EmailMessage()
    # msg['Subject'] = subject
    # msg['From'] = email
    # msg['To'] = receiver_email
    # msg.set_content(text)
    #
    # with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    #     smtp.login(email, password)
    #     print("Logged in")
    #     smtp.send_message(msg)
    #     print("email sent")

def result_generation(gene_choice: str, organism_choice: str, list_in_common: list):
    results = f"""
    Results for Gene: {gene_choice}, Organism ID: {organism_choice}.
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