from flask_mail import Message

def send_message(mail_instance, name, email, institution, country, message):
    '''
    Processes a mail message using the function's arguments 
    and sends a message to app's email.
    '''
    try:
        msg = Message(subject = '[ColabAtlas] Pending Message', sender = email, recipients = ['8116da10dbe882'])
        msg.body = f'''
        A new message from ColabAtlas has been received with the following details: \n\nName: {name}\nEmail: {email}\nSender's Institution: {institution}\nCountry: {country}\n\nMessage:\n{message}
        '''.lstrip()
        mail_instance.send(msg)
        return None
    except Exception as e:
        return(str(e))