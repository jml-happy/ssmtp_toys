# https://variax.wordpress.com/2017/03/07/send-mail-from-raspberry-pi-command-line-andor-python-script/

import smtplib

smtpUser = 'myEmailAddress@gmail.com'
smtpPass = 'superSecretPassword'
toAdd = 'theToEmailAddress@hotmail.com'
fromAdd = smtpUser
subject = 'Python Test'
header = 'To: ' + toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Subject: ' + subject
body = 'From within a Python script'
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.ehlo()
s.login(smtpUser, smtpPass)
s.sendmail(fromAdd, toAdd, header + '\n\n' + body)
s.quit()
