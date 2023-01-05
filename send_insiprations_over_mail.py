import requests
import os
import smtplib
from email.message import EmailMessage


def quote_author():
#sends request and collects quote and author
    quotes_info = requests.get("https://zenquotes.io/api/quotes/").json()[0]
    quote = quotes_info['q']
    author = quotes_info['a']
    return quote, author

#Email log in details 
email_address = os.environ.get('EMAIL_ADDRESS')
email_receiver = ["email_list"] #do not forget to add actual emails
# one needs to add two-step verification for this to  work
email_pass = os.environ.get('EMAIL_PASS') 

# settings of the mail form 
message = EmailMessage()
message['From'] = email_address
message['To'] = email_receiver
message['Subject'] = "Inspiring quotes"
#the content of the mail
message.set_content(f"You might face all possible problems in your life but do not forget that you are not alone.\nAs the great {quote_author()[1]} once said:\n\"{quote_author()[0]}\"")

#mail algorithm that sends content from and to email.
if __name__ == "__main__":
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(email_address, email_pass)
        smtp.sendmail(email_address, email_receiver, message.as_string())
