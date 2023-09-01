# import smtplib
#
#
# MY_EMAIL = "trakerprice@gmail.com"
# password = "okdsrlmcckzhsvzb"
#
#
#
# def send(name, email):
#     message = f"Subject:تطبيقة اقتراحات الولي\n\nمرحبا {name}\nتم تلقي اقتراحكم بنجاح سنطواصل معكم قريبا"
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=MY_EMAIL, password=password)
#         connection.sendmail(from_addr=MY_EMAIL, to_addrs=email, msg=message)
#
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

MY_EMAIL = "trakerprice@gmail.com"
password = "okdsrlmcckzhsvzb"

def send(name, email):
    # Create a message container
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "تطبيقة اقتراحات الولي"
    msg['From'] = MY_EMAIL
    msg['To'] = email

    # Create the text part of the message
    text = f"مرحبا {name}\nتم تلقي اقتراحكم بنجاح سنتواصل معكم قريبا"
    text_part = MIMEText(text.encode('utf-8'), 'plain', 'utf-8')
    msg.attach(text_part)

    # Connect to the SMTP server
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=password)

        # Send the email
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=email, msg=msg.as_string())

