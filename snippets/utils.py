import threading
from django.core.mail import send_mail

class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        threading.Thread.__init__(self)

    def run (self):
        # msg = EmailMessage(self.subject, self.html_content, EMAIL_HOST_USER, self.recipient_list)
        # msg.content_subtype = "html"
        # msg.send()
        send_mail(
        self.subject,
        self.html_content,
        'dir@tony850421.webfactional.com',
        [self.recipient_list]
        )

def send_html_mail(subject, html_content, recipient_list):
    EmailThread(subject, html_content, recipient_list).start()