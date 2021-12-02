import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail():
    url = 'smtp.mail.ru'

    login = input('свой mail: ')
    password = input('свой password')
    toaddr = input('Кому отправить?: ')
    topic = input('Тема или название: ')
    message = input('Сообщение: ')

    msg = MIMEMultipart()

    msg['Subject'] = topic
    msg['From'] = login
    body = message
    msg.attach(MIMEText(body, 'plain'))

    server = root.SMTP_SSL(url, 465)
    server.login(login, password)
    server.sendmail(login, toaddr, msg.as_string())
    input()

def main():
    send_mail()


if __name__ == '__main__':
    main()
