# POP-MailServer
POP-II Project

This is a simple email client web application. This also includes a custom SMTP server written using Python's SMTPD library.
The client can compose, send and view sent mails.

# Set up
First run the django development server
```sh
python manage.py runserver
```
Then start the SMTP server on `/server` URL.

Then the client can be opened at `/`
