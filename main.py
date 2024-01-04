import smtplib
import pandas
import random
import datetime as dt


my_email = 'testingpython610@gmail.com'
password = 'nhiwusmbzwtrdrwt'
date = dt.datetime.now()
today = (date.month, date.day)
data = pandas.read_csv('birthdays.csv')
data_dict = data.to_dict('records')
file_path = f'letter_templates/letter_{random.randint(1,3)}.txt'

with open(file_path) as letters:
    letter = letters.read()

for i in data_dict:
    if today == (i['month'], i['day']):
        name = i['name']
        new_letter = letter.replace('[NAME]', name)

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs='testingpython17463@yahoo.com',
                msg=f'Subject:Happy Birthday!!!!\n\n{new_letter}'
            )
