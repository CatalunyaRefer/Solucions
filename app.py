from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
app.secret_key="1234"

app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'apelaezia@insjoaquimmir.cat'
# app.config['MAIL_PASSWORD'] = 'alexpamir03'
# app.config['MAIL_USERNAME'] = 'info@solucions.org'
# app.config['MAIL_PASSWORD'] = 'Red11red'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
recipient_email = os.getenv('RECIPIENT_EMAIL')

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        sender_email = request.form['email']
        message_body = request.form['message']

        msg = Message("New Contact Form Submission",
                    sender=app.config['MAIL_USERNAME'],  
                    recipients=[recipient_email],
                    reply_to=sender_email)
        msg.body = message_body 

        try:
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')

        return redirect(url_for('home')) 
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        sender_email = request.form['email']
        message_body = request.form['message']

        msg = Message(f"From {sender_email}",
                    sender=app.config['MAIL_USERNAME'], 
                    recipients=[recipient_email],
                    reply_to=sender_email)
        msg.body = message_body 


        try:
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')

        return redirect(url_for('contact')) 
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/vilanova')
def vilanova():
    return render_template('vilanova.html')

@app.route('/vendrell')
def vendrell():
    return render_template('vendrell.html')

@app.route('/roquetes')
def roquetes():
    return render_template('roquetes.html')

@app.route('/about')
def about_us():
    return render_template('about_us.html')