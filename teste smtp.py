import smtplib

sender_email = 'leo07tonolli@gmail.com'
rec_email =  'leo07tonolli@gmail.com'
password = "1507Bela"
message = "Hey there"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("Conectado")
server.sendmail(sender_email, rec_email, message)
print("Email enviado")
