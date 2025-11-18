import smtplib
import ssl
import os
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Email details
email_sender = "douglas.london@ucas-edu.net"  # Replace with your email address
email_receiver = "douglas.london@ucas-edu.net"  # Replace with the recipient's email address
email_password = "fjlp luur itcn mcgz"  # Replace with generated app password
subject = "Email with Attachment"
body = "This email has an attachment."

msg = MIMEMultipart()
msg['Subject'] = subject
msg['From'] = email_sender
msg['To'] = email_receiver

msg.attach(MIMEText(body, 'plain'))

filename = "screenshot.png"  # If want to send image then file path here

# Open the file in binary read mode
try:
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attach part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Attach the file to the email
    msg.attach(part)

except FileNotFoundError:
    print(f"Error: {filename} not found.")
    exit()

# SMTP server details
smtp_server = "smtp.gmail.com"
port = 465
context = ssl.create_default_context()

# Send the email
try:
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(email_sender, email_password)
        server.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")
