#
import smtplib
import requests
import json

responseFromISS = requests.get("http://api.open-notify.org/iss-now.json") # Get Json Data
responseFromISS.raise_for_status()
dataISS = responseFromISS.json()
print(dataISS)

#34.281757, -77.852928
parameter = {
    "lng": -77.946200,
    "lat": 34.236700

}
response = requests.get("https://api.sunrise-sunset.org/json",params=parameter)
data = response.json()
print(data)


# if parameter["lat"] == dataISS['iss_position']["latitude"]




# myEmail = "vde821149@gmail.com"
# connection =smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=myEmail,password="deVan123")
# connection.sendmail(from_addr=myEmail,to_addrs="nghia.van0910@gmail.com",msg="Hello")
# connection.close()
