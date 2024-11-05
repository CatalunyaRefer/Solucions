from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)

app.secret_key="1234"

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'apelaezia@insjoaquimmir.cat'
app.config['MAIL_PASSWORD'] = 'alexpamir03'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        sender_email = request.form['email']
        message_body = request.form['message']

        msg = Message("New Contact Form Submission",
                      sender=sender_email, 
                      recipients=['apelaezia@insjoaquimmir.cat'])
        msg.body = message_body 

        try:
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')

        return redirect(url_for('home')) 

    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)

@app.route('/vilanova', methods=['GET', 'POST'])
def vilanova():
        if request.method == 'POST':
            sender_email = request.form['email']
            message_body = request.form['message']

            msg = Message("New Contact Form Submission",
                        sender=sender_email, 
                        recipients=['apelaezia@insjoaquimmir.cat'])
            msg.body = message_body 

            try:
                mail.send(msg)
                flash('Your message has been sent successfully!', 'success')
            except Exception as e:
                flash(f'Error: {str(e)}', 'error')

            return redirect(url_for('vilanova')) 

        return render_template('vilanova.html')

@app.route('/vendrell', methods=['GET', 'POST'])
def vendrell():
    if request.method == 'POST':
        sender_email = request.form['email']
        message_body = request.form['message']

        msg = Message("New Contact Form Submission",
                      sender=sender_email, 
                      recipients=['apelaezia@insjoaquimmir.cat'])
        msg.body = message_body 

        try:
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')

        return redirect(url_for('vendrell')) 

    return render_template('vendrell.html')

@app.route('/roquetes', methods=['GET', 'POST'])
def roquetes():
    if request.method == 'POST':
        sender_email = request.form['email']
        message_body = request.form['message']

        msg = Message("New Contact Form Submission",
                      sender=sender_email, 
                      recipients=['apelaezia@insjoaquimmir.cat'])
        msg.body = message_body 

        try:
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')

        return redirect(url_for('roquetes')) 

    return render_template('roquetes.html')
