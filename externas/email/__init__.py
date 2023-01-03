def envio(txt):
    from PySimpleGUI import PySimpleGUI as sg
    import smtplib
    from email.message import EmailMessage
    from externas import dados

    EMAIL_ADDRESS = dados.Email
    EMAIL_PASSWORD = dados.Senha

    msg = EmailMessage()
    msg['subject'] = 'Sugestões'
    msg['From'] = dados.Email
    msg['To'] = dados.Email
    msg.set_content(txt)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            smtp.send_message(msg)
            return True
    
    except TimeoutError:
        return 'Verifiqeu sua conecção'
        
    except Exception as erro2:
        sg.popup_error(erro2, no_titlebar= True)