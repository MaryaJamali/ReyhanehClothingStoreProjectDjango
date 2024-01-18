from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def send_email(subject, to, context, template_name):
    try:
        # Combining template and context and converting it to a text string with render_to_string
        html_message = render_to_string(template_name, context)
        # It optimizes the tag structure of html_message
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, plain_message, from_email, [to], html_message=html_message)
    except:
        pass
