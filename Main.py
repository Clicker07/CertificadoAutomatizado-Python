import pandas as pd
import tratamento_de_imagem as tdi

# LER A TABELA NO EXCEL
x = pd.read_excel(r"C:\Certificado_automatizado\tabela.xlsx")

# LER O NUMERO DE LINHAS DE COLUNAS
l = x.shape

# IMPRESSÃO DOS CERTIFICADOS
for i in range(0,l[0]):

    tdi.gerar_certificado(x['Nomes'] [i])








