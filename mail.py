import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# Connect to Gmail SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

#Reading the password from password.txt file
with open("password.txt", "r") as f:
    password = f.read()

# Login to Gmail SMTP server
server.login("*******@gmail.com", password)

# Create a multipart message
msg = MIMEMultipart()
msg["From"] = "Bett"
msg["To"] = "*******gmail.com"
msg["Subject"] = "GREETINGS"

# Read the message content
with open("message.txt", "r") as f:
    message = f.read()

# Attach the message to the email
msg.attach(MIMEText(message, "plain"))

# Attach the image file
filename = "pic.jpg"
with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)
part.add_header("Content-Disposition", f"attachment; filename= {filename}")
msg.attach(part)

# Send the email
#Note enter the senders email receiver email
server.sendmail("sender Email", "Receiver Email", msg.as_string())

# Quit the server
server.quit()
