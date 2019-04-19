import os.path
import atar
import java
import psql
import datetime
import smtplib
import artemis

MAIL_SUBJECT = "ATAR IS DOWN"
MAIL_SMTP_HOST = "smtp.gmail.com"
MAIL_SMTP_PORT = "587"
MAIL_SMTP_USER = "atarbce@gmail.com"
MAIL_SMTP_PASSWD = "atar1q2w3e4r"
MAIL_SMTP_TO = "barkancanerdogdu@gmail.com"

if not os.path.isfile("downfall"):
	atar.Atar().version()
	atarservice = atar.Atar().service()
	artemisservice = artemis.Artemis().service()
	postgresqlservice = psql.Psql().service()
	if not atarservice[0] or not atarservice[1] or not artemisservice[0] or not postgresqlservice[0]:
		psql.Psql().version()
		artemis.Artemis().broker_xml()
		artemis.Artemis().artemis_profile()
		artemis.Artemis().context_xml()
		file = open("downfall","w+")

		context = atarservice[2] + atarservice[3] + artemisservice[2] + artemisservice[3] + artemisservice[4] + artemisservice[1] + postgresqlservice[2] + postgresqlservice[1] + java.Java(file).version() + str(datetime.datetime.now()) + "\n"

		file.write(context)
		file.close()
		
		mail_context = 'Subject: {}\n\n{}'.format(MAIL_SUBJECT,context)
		
		mail = smtplib.SMTP(MAIL_SMTP_HOST,MAIL_SMTP_PORT)
		mail.ehlo()
		mail.starttls()
		mail.login(MAIL_SMTP_USER,MAIL_SMTP_PASSWD)
		mail.sendmail(MAIL_SMTP_USER,MAIL_SMTP_TO,mail_context)
		mail.close()
