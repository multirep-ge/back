from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.utils.html import strip_tags


def send_confirmation_email(email, token_id, user_id):
    data = {
        'token_id': str(token_id),
        'user_id': str(user_id)
    }
    html_message = get_template('mail_body.html').render(data)
    plain_message = strip_tags(html_message)
    subject = 'Please confirm your email'
    from_email = 'wpapuna1995@gmail.com'
    recipient_list = [email]
    email_message = EmailMultiAlternatives(
        subject=subject,
        body=plain_message,
        from_email=from_email,
        to=recipient_list
    )
    email_message.attach_alternative(html_message, 'text/html')
    email_message.send()


def send_password_reset_instruction(email, token_id):
    data = {
        'token_id': str(token_id),
    }
    html_message = get_template('password_reset_email.html').render(data)
    plain_message = strip_tags(html_message)
    subject = 'პაროლის შეცვლის ინსტრუქცია'
    from_email = 'wpapuna1995@gmail.com'
    recipient_list = [email]
    email_message = EmailMultiAlternatives(
        subject=subject,
        body=plain_message,
        from_email=from_email,
        to=recipient_list
    )
    email_message.attach_alternative(html_message, 'text/html')
    email_message.send()







