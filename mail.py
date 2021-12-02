import smtplib as root
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def mail_ru():
    url = 'smtp.mail.ru'

    login = 'rupit.cod@mail.ru'
    password = 'Qazwsxedc271'
    toaddr = 'rupit.cod@mail.ru'

    topic = 'Код'
    message = 'Код для подтверждения вашего аккаунта на сайте RuPit: '

    msg = MIMEMultipart()

    msg['Subject'] = topic
    msg['From'] = login
    body = message
    msg.attach(MIMEText(body, 'plain'))

    server = root.SMTP_SSL(url, 465)
    server.login(login, password)
    server.sendmail(login, toaddr, msg.as_string())


if __name__ == '__mail__':
    mail_ru()

    while True:
        a = [a for a in range(1000000)]
        mail_id = random.choice(a)
        if User.mail != mail_id:
            user = User(
                login=form.login.data,
                hashed_password=form.password.data,
                mail=form.mail.data,
                mail_id=mail_id
            )
            break