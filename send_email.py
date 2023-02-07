import smtplib

def sendEmail(mesaj):
	myemail = "mailadresiniz@gmail.com"
	mypassword = "şifreniz"
	connection = smtplib.SMTP("smtp.gmail.com", 587)
	connection.starttls()
	connection.login(user= myemail, password= mypassword)


	connection.sendmail(from_addr= myemail,
						to_addrs= "gonderilecek@gmail.com",
						msg = mesaj)
	connection.close()