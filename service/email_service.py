import smtplib
from config import EMAIL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from validate_email import validate_email


class EmailService:
    def __init__(self):
        pass

    @staticmethod
    def filter_mail(email_string):
        if email_string is None:
            return ""

        return ",".join(
            [
                mail
                for mail in email_string.split(",")
                if validate_email(
                    email_address=mail,
                    smtp_from_address=EMAIL["ID"] + "@" + EMAIL["SERVER"],
                )
            ]
        )

    @staticmethod
    def receiver(*types):
        receivers = []
        for users in types:
            if users is None:
                break

            receivers += users.split(",")
        return receivers

    @staticmethod
    def send(to, cc, bcc, subject, text, html):
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = EMAIL["FROM"]
        message["To"] = to
        message["Cc"] = cc

        if html:
            body = MIMEText(html, "html")
        else:
            body = MIMEText(text)
        message.attach(body)

        server = smtplib.SMTP(EMAIL["SERVER"], EMAIL["PORT"])
        server.set_debuglevel(1)

        server.sendmail(
            EMAIL["EMAIL"],
            EmailService.receiver(to, cc, bcc),
            message.as_string(),
        )
        server.quit()

        return {
            "to": to,
            "cc": cc,
            "bcc": bcc,
            "subject": subject,
            "text": text,
            "html": html,
        }
