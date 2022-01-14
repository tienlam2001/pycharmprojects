import smtplib
import pandas
from random import randrange


for i in range(50):
    data = pandas.read_csv("data/quoteconvert.csv")
    quotes = data.to_records()
    print(quotes[1][2])
    
    myemail = "vde821149@gmail.com"
    connection =smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=myemail,password="deVan123")
    connection.sendmail(from_addr=myemail,to_addrs="nghia.van0910@gmail.com",msg=f'Subject:Quote For The Day \n\n {quotes[randrange(0,len(quotes))][2]}')
    connection.close()
# dataQuote = open("data/quote.txt")
# data = pandas.DataFrame(dataQuote)
# dataConvert.to_csv("data/quoteconvert.csv")