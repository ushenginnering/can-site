import subprocess
import os
from django.core.mail.backends.base import BaseEmailBackend
from django.conf import settings

class PHPMailBackend(BaseEmailBackend):
    def send_messages(self, email_messages):
        for email_message in email_messages:
            subject = email_message.subject
            body = email_message.body
            recipient_email = email_message.to[0]  # Assuming single recipient

            self.send_email_via_php(subject, body, recipient_email)
        return len(email_messages)

    def send_email_via_php(self, subject, message, recipient_email):
        try:
            result = subprocess.run(
                ['php', os.path.join(settings.BASE_DIR, 'send_email.php'), subject, message, recipient_email],
                capture_output=True,
                text=True
            )
            if result.returncode != 0:
                raise Exception(f"Failed to send email: {result.stderr}")
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")