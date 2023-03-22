
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
34     to_addresses = ['E-Mail@Example.com', 'E-Mail@Example.com', 'E-Mail@Example.com'] >> Change The E-Mails Value to The E-mails that U Need to Send Mails to Them, and make sure there are in [] Every mail in '' with , after ' i hope you understand :D
35     subject = "Mail Subject" >> Change "Mail Subject" with Your Subject
36     message = "Mail Message" >> Change "Mail Message" With Your "Message" you can use \n to go to the next line
37     attachment_path = 'File/Path.pdf' >> Change "File/Path.pdf" with your name of file u need to attachment it, if the file at the same folder with py code, or enter it Path from your PC if it dose not exist in folder of py project.

```
## Demo

Insert gif or link to demo


## Optimizations

in order that when We Try to Send More and More E-Mails, Application will stop trmporary because spamming issue, we have to open the code and remove the mail that we have send to it, then try run application later.

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
- [@Eslam Mustafa](https://github.com/LeaDer-E/)


## Cridit

- Copyright © Eslam Mustafa 🌹


♥ I hope you like my Simple Code, thank you ♥
