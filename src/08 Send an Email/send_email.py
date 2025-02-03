import smtplib
import os


def send_email(smtp_config, email_message):
    message = f"Subject: {email_message['subject']}"
    "\n\n"
    f"{email_message['body']}"

    with smtplib.SMTP_SSL(smtp_config['host'], smtp_config['port']) as server:
        server.login(smtp_config['uname'], smtp_config['pwd'])
        server.sendmail(smtp_config['uname'], email_message['recipient'], message)


# commands used in solution video for reference
if __name__ == '__main__':
    # replace receiver email address
    smtp_config = {
        'host': 'smtp.gmail.com',
        'port': 465,
        'uname': os.environ.get('GMAIL_USERNAME', 'my_email@gmail.com'),
        'pwd': os.environ.get('GMAIL_PWD', 'MyComplicatedPwd@1234')  # Enable 2FA and use App Pwd here
    }

    email_message = {
        'recipient': 'somerecipient@gmail.com',
        'subject': 'Test Email',
        'body': 'Hi, Nice meeting you!'
    }

    send_email(smtp_config, email_message)
