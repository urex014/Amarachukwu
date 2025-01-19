from flask import Flask, request, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_email_password'

mail = Mail(app)

# Route for the contact form page
@app.route('/')
def contact_form():
    return render_template('contact_form.html')  # Save the HTML above as contact_form.html

# Route to handle form submission
@app.route('/send', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    message_body = request.form['message']

    try:
        # Compose the email
        msg = Message(
            subject=f"New Message from {name}",
            sender=email,
            recipients=["your_email@example.com"],  # Replace with your email
            body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_body}"
        )
        mail.send(msg)
        return "Message sent successfully!"
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '_main_':
    app.run(debug=True)