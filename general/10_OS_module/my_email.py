import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Replace these with appropriate values
sender_email = "halder.gourav@gmail.com"
receiver_email = "gourav.halder@kingfisher.com"
#password = "gmail_1981"
password= 'eacp nlnd ltqy wats'
# Create the email headers and content
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Test Email from Python"

# Email body
body = "This is a test email sent from Python script."
message.attach(MIMEText(body, "plain"))

try:
    # Connect to the Gmail SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # Secure the connection
    server.login(sender_email, password)  # Log in to your Gmail account

    # Send the email
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
finally:
    server.quit()  # Close the connection
