from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        email = request.form['email']
        message = request.form['message']
        
        msg = Message('Contact Form Message', recipients=['apelaezia@insjoaquimmir.cat'])  # Replace with your recipient email
        msg.body = f'Email: {email}\n\nMessage:\n{message}'
        
        try:
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
            return redirect(url_for('contact'))
        except Exception as e:
            flash('An error occurred while sending your message. Please try again later.', 'error')
            print(e)

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
