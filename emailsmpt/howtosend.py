# Fake Gmail Account
# vde821149@gmail.com
# deVan123

# Fake gmail Account
#nsu8728@gmail.com
#HiBaBON123

import smtplib
myEmail = "vde821149@gmail.com"
connection =smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=myEmail,password="deVan123")
connection.sendmail(from_addr=myEmail,to_addrs="nghia.van0910@gmail.com",msg="Hello")
connection.close()