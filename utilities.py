import smtplib
from email.message import EmailMessage


def send_mail(send_to, subject, text):
    email = "ashevans3000@gmail.com"
    password = "test3000"
    reciever_email = send_to
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