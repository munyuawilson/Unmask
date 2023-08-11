import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def sendEmail(name,sender_email,message):
    # Email configuration
    
    receiver_email = 'wmunyua4@gmail.com'
    subject = f'{name}: Query from Unmask '
    
    message=sender_email + "\n" + message
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Add the message body
    msg.attach(MIMEText(message, 'plain'))

    # SMTP server configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'wmunyua4@gmail.com'
    smtp_password = 'hmmvqjihdnxrlsda'

    try:
        # Create a SMTP session and connect to the server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.connect(smtp_server, smtp_port)

        # Start TLS encryption
        server.starttls()

        # Login to the SMTP server
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print('Email sent successfully!')

    except Exception as e:
        print('Error sending email:', str(e))

    finally:
        # Close the SMTP session
        if server:
            server.quit()
