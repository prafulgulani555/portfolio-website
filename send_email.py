import smtplib, ssl
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "prafulgulani555@gmail.com"
    password = os.getenv("Password")
    context = ssl.create_default_context()
    receiver = ""
    message = """

    """
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

