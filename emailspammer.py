import csv
import smtplib
from time import sleep
from configparser import ConfigParser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

with open('info.csv', 'r', encoding='UTF-8') as file:
    reader = csv.DictReader(file, delimiter=',')
    data = [line for line in reader]
print(data)
config = ConfigParser()
config.read('config.ini')

host = config.get('smtp', 'server')
login = config.get('smtp', 'user')
password = config.get('smtp', 'password')
subject = 'Hello, it`s a test'
timing = int(config.get('smtp', 'timing'))

f = open('main.html', 'r')
text = f.read()
print(text)

server = smtplib.SMTP(host)
server.ehlo()
server.starttls()
server.ehlo()
server.login(login, password)

for key in data:
    msg = MIMEMultipart()
    msg.attach(MIMEText(text, 'html', 'UTF-8'))
    msg['Subject'] = subject
    msg['From'] = login

    server.sendmail(login, key['email'], msg.as_string())
    sleep(timing)
server.quit()