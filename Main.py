import pandas as pd
import tratamento_de_imagem as tdi
import enviar_email as libmail
import getpass

# LER A TABELA NO EXCEL
x = pd.read_excel(r"C:\CertificadoAutomatizado-Python\tabela.xlsx")

# LER O NUMERO DE LINHAS DE COLUNAS
l = x.shape

password_email = getpass.getpass("E-mail Password: ")

# IMPRESSÃO DOS CERTIFICADOS
for i in range(0,l[0]):
    tdi.gerar_certificado(x['Nome_certificado'] [i])

#Envio de email
for i in range(0,l[0]):
    libmail.send_email(x['Nome'] [i],x['Email'] [i],x['Nome_certificado'] [i],password_email)










