from django.core.mail import send_mail

def send_match_notification(user_email, match_info):
    subject = 'Potential Match Found'
    message = f'Hello, we found a potential match: {match_info}'  # Customize the message as needed
    send_mail(subject, message, 'from_email@example.com', [user_email])  # Send the email
