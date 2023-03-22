import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import time

print("Outlook-Bulk v1.0.0")
print("Created By Eslam-Mustafa. \n Linked in: https://www.linkedin.com/in/LeaDer-E/ \n I hope you like it")

def send_email(to_addresses, subject, message, attachment_path):
    # Set up the email message
    msg = MIMEMultipart()
    msg['From'] = 'Your_Email_Or_User_Name'
    msg['To'] = ', '.join(to_addresses)
    msg['Subject'] = subject

    # Add the message to the email
    body = MIMEText(message)
    msg.attach(body)

    # Add the attachment to the email
    with open(attachment_path, 'rb') as f:
        attachment = MIMEApplication(f.read(), _subtype='pdf')
        attachment.add_header('Content-Disposition', 'attachment', filename='File_Name.pdf')
        msg.attach(attachment)

    # Connect to the SMTP server and send the email
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login('Your_Email@outlook.com', 'Your_Password!')
    server.sendmail('Your_Email@outlook.com', to_addresses, msg.as_string())
    server.quit()

# Example usage
to_addresses = ['E-Mail@Example.com', 'E-Mail@Example.com', 'E-Mail@Example.com']
subject = "Mail Subject"
message = "Mail Message"
attachment_path = 'File/Path.pdf'
for address in to_addresses:
    send_email([address], subject, message, attachment_path)
    print("[+] Mail Sended to :", address," ^.^")
    time.sleep(5)

