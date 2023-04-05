
# Outlook-Bulk-Mails-Sender

A simple smtplib email program to sending Emails with attaching One File and send every E-Mail Alone that only works with Outlook



## Installation

Just make Sure U Have Python on Your PC.

### Mac:
```bash
  brew update && brew upgrade python 
```

### Linux & Unix:
```bash
  sudo apt-get install python3 
```
    
### Windows x64 bit:

Download from [Here x64][Here x64]

[Here x64]: https://www.python.org/ftp/python/3.10.10/python-3.10.10-amd64.exe


### Windows x32 & x86 bit:
Download from [Here x32 & x86][Here x32 & x86]

[Here x32 & x86]: https://www.python.org/ftp/python/3.10.10/python-3.10.10.exe

### Android OS:
Download from [Here Android][Here Android]

[Here Android]: https://play.google.com/store/apps/details?id=ru.iiec.pydroid3&hl=en&gl=US&pli=1

<mark>Not Tested</mark>

### IOS:
Download from [Here IOS][Here IOS]

[Here IOS]: https://apps.apple.com/us/app/python3ide/id1357215444

<mark>Not Tested</mark>
## How to Use Application:

### Open Outlook-Bulk-Mails-Sender.py
Change The Lines Above:
```bash
12     msg['From'] = 'Your_Email_Or_User_Name' >> With Your Email or User Name;
22     attachment = MIMEApplication(f.read(), _subtype='pdf') >> Change The _subtype from 'pdf' to any, if The File are With Other Type Like Docx, or xlsx, or pptx, or any other type
23     attachment.add_header('Content-Disposition', 'attachment', filename='File_Name.pdf') >> Change 'File_Name.pdf' to the name of the file you that will be in the Sending Mail.
29     server.login('Your_Email@outlook.com', 'Your_Password!') >> Change Your_Email With Your Read E-Mail, And Your_Password With Your Read Password
30     server.sendmail('Your_Email@outlook.com', to_addresses, msg.as_string()) >> also Change Your_Email To Your Read E-Mai
34     to_addresses = ['E-Mail@Example.com', 'E-Mail@Example.com', 'E-Mail@Example.com'] >> Change The E-Mails Value to The E-mails that U Need to Send Mails to Them, and make sure there are in [] Every mail in single or duble quotation, i hope you understand :D
35     subject = "Mail Subject" >> Change "Mail Subject" with Your Subject
36     message = "Mail Message" >> Change "Mail Message" With Your "Message" you can use \n to go to the next line
37     attachment_path = 'File/Path.pdf' >> Change "File/Path.pdf" with your name of file u need to attachment it, if the file at the same folder with py code, or enter it Path from your PC if it dose not exist in folder of py project.

```

## Attach Two Files:
To attach two files as PDF, you can modify the `send_email` function to accept a list of attachment paths instead of a single path. Then, you can iterate over the attachment paths and attach each file to the email.
Here's an updated version of the `send_email` function that can handle multiple attachments:
```bash
def send_email(to_addresses, subject, message, attachment_paths):
    # Set up the email message
    msg = MIMEMultipart()
    msg['From'] = 'Your_Email_Or_User_Name'
    msg['To'] = ', '.join(to_addresses)
    msg['Subject'] = subject

    # Add the message to the email
    body = MIMEText(message)
    msg.attach(body)

    # Add the attachments to the email
    for attachment_path in attachment_paths:
        with open(attachment_path, 'rb') as file:
            attachment = MIMEApplication(file.read(), _subtype='pdf')
            attachment.add_header('Content-Disposition', 'attachment', filename='File_Name.pdf')
            msg.attach(attachment)

    # Connect to the SMTP server and send the email
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login('Your_Email@outlook.com', 'Your_Password!')
    server.sendmail('Your_Email@outlook.com', to_addresses, msg.as_string())
    server.quit()
```

To use this function to send an email with two attachments, you can call it like this:

```bash
to_addresses = ['E-Mail@Example.com', 'E-Mail@Example.com', 'E-Mail@Example.com']
subject = "Mail Subject"
message = "Mail Message"
attachment_paths = ['File/Path1.pdf', 'File/Path2.pdf']
for address in to_addresses:
    send_email([address], subject, message, attachment_paths)
    print("[+] Mail Sended to :", address," ^.^")
    time.sleep(5)
```

This code will attach both `File/Path1.pdf` and `File/Path2.pdf` to the email message.

## Demo
![My Video2](https://user-images.githubusercontent.com/99460904/227059434-d9e3efe3-1bc5-429b-b456-f9628df0fe36.gif)
![ezgif com-video-to-gif (1)](https://user-images.githubusercontent.com/99460904/227000086-94db699a-dfe0-4b58-82ab-cf0a10b2efa2.gif)

## Screenshot
![image](https://user-images.githubusercontent.com/99460904/226981595-eaf352c4-4e88-439c-9c5c-1a690e3c350f.png)

## Speed and Duration:
* 430 Mail Takes 50 Min.
* 1 Mail\7 Secounds

## Tutorial
### Vedio on youtube
[![Watch the video](https://user-images.githubusercontent.com/99460904/179158938-e161db4b-c111-446a-ab21-0da683a6e8d2.png)](https://youtu.be/bXov3q9xgwI)

## Optimizations

in order that when We Try to Send More and More E-Mails, Application will stop trmporary because spamming issue, we have to open the code and remove the mail that we have send to it, then try run application later.
Watch out From: We've noticed some unusual activity in your Outlook account. To help protect you, we've temporarily blocked it. Please verify your account. 
You can verify and problem will be resolve and you can use the program again

### Fixing

![image](https://user-images.githubusercontent.com/99460904/227046565-d87ebb12-6574-4ebc-9692-266b90078e6c.png)

"If you receive an error message indicating that your email has been blocked, you can try to unblock it by verifying your phone number. This can be done using the Microsoft Edge browser. If you are unsure about how to do this, You can take a look about this [Topic][Topic]. It is a Easy process, so there's no need to worry. If you are still hesitant, you could also consider creating a new account to use the tool."

[Topic]: https://support.microsoft.com/en-us/account-billing/account-has-been-locked-805e8b0d-4141-29b2-7b65-df6ff6c9ce27


## Appendix

* I have been add time to sleep some seconds between every E-Mail, that can hold the remporary banned some little.

## Known Issues
Any issues are usually because the underlying browser automation framework has a
bug or inconsistency. Where possible, we try to cover up these underlying
problems in the client, but sometimes workarounds require higher-level
intervention.
try to restart the code or change the vedio link
Please feel free to file an [issue][issue] if this client doesn't work as
expected.

[issue]: https://github.com/LeaDer-E/Outlook-Bulk-Mails-Sender/issues/new

## Author's name.
- [@Eslam Mustafa](https://www.linkedin.com/in/LeaDer-E/)

## Cridit

- Copyright © Eslam Mustafa 🌹


♥ I hope you like my Simple Code, thank you ♥
