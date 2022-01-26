from django.core.mail import send_mail
from django.conf import settings
from smtplib import SMTPException

def sendEmails(bulkEmailObj):
    try:
        send_mail(
            bulkEmailObj.subject,
            bulkEmailObj.content,
            settings.EMAIL_HOST_USER,
            bulkEmailObj.recipients,
            fail_silently=False,
        )
        return True
    except SMTPException as e:
        return e