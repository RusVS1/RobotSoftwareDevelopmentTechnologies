import smtplib
import os
import json
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

sender_email = os.getenv("SENDER_EMAIL")
sender_password = os.getenv("SENDER_PASSWORD")
recipient_email = os.getenv("RECIPIENT_EMAIL")

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = "Test email"

with open("message.json", "r", encoding="utf-8") as f:
    message_data = json.load(f)

name = message_data["name"]
task = message_data["task"]


html = f"""\
<html>
  <head></head>
  <body>
    <h2>Hi!</h2>
    <p>My name is <i>{name}</i>, and my task is {task}.</p>
  </body>
</html>
"""

message.attach(MIMEText(html, "html", "utf-8"))

server = smtplib.SMTP("smtp.mail.ru", 587)
server.starttls() 
server.login(sender_email, sender_password)
server.sendmail(sender_email, recipient_email, message.as_string())
server.quit()
