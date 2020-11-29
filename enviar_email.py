import smtplib
import getpass
import unicodedata
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

def send_email(nome, email_to,nomearq,password):
    """
        Função na qual envia o email anexado
        para o participante
        :param nome: Entre com o nome do participante
        :param email_to: Email para qual deve ser enviado o arquivo
    """
    nomearq = nomearq.replace(" ", "_")
    nome = unicodedata.normalize('NFD',nome).encode('ascii', 'ignore')

    msg = MIMEMultipart()

    email_from = 'leo07tonolli@gmail.com'
    msg['Subject'] = 'Certificado Palestra'
    message = f'''EMAIL TESTE PYTHON
    Hey {nome.decode()},\n\n 
    Segue anexado o certificado da palestra. Obrigado por participar!!\n
    Att,
    Leonardo Tonolli'''

    msg.attach(MIMEText(message, 'plain'))

    filename = f"Certificado_{nome.decode()}.png"

    try:
        attachment = open(f'Certificado_{nomearq}.png', 'rb')
    except FileNotFoundError:
        print("Arquivo de anexo não encontrado, verifique e tente novamente")
        quit()

    part = MIMEBase('image', 'png')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename= {filename}")

    msg.attach(part)
    msg = msg.as_string()


    server = 0

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

    finally:
        server.quit()



