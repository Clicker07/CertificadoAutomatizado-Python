import smtplib
import getpass
import unicodedata
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
"""
    Função na qual envia o email anexado
    para o participante
    :param nome: Entre com o nome do participante
    :param email_to: Email para qual deve ser enviado o arquivo
"""
#def send_email(nome, email_to):



nome = "Léonardo"
nome = unicodedata.normalize('NFD',nome).encode('ascii', 'ignore')

email_from = 'leo07tonolli@gmail.com'
email_to = 'leo07tonolli@gmail.com'
password = getpass.getpass("E-mail Password: ")
message = f'''Subject: CERTIFICADO PALESTRA
Hey {nome.decode()},\n\n 
Segue anexado o certificado da palestra. Obrigado por participar!!\n
Att,
Leonardo Tonolli'''

msg = MIMEMultipart()
msg.attach(MIMEText(message, 'plain'))

filename = "Exemplo Certificado.png"
attachment = open('Exemplo Certificado.png', 'rb')

part = MIMEBase('application', 'png')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)


server = 0
foto = open(r"C:\CertificadoAutomatizado-Python\Certificado_Leo.png")
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
except:
    print("Erro ao conectar ao servidor, verifique a conexão e tente novamente")
    exit()

try:
    server.login(email_from, password)
    print("Conectado ao servidor")
except smtplib.SMTPAuthenticationError:
    print("Senha ou usuario incorretos, verifique e tente novamente.")

try:
    server.sendmail(email_from, email_to, msg)
    print("Email enviado")
except smtplib.SMTPRecipientsRefused:
    print("Endereço email do destinario invalido")




#send_email("Leonardo", "leo07tonolli@gmail.com")
