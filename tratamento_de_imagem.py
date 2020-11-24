from PIL import Image, ImageDraw, ImageFont

"""Tratamento de imagem - Desenha o nome da pessoa no certificado"""

def gerar_certificado(nome):
    """
    Função na qual gera um certificado,
    abrindo a imagem selecionada como background
    e escrevendo por cima
    :rtype: object
    :param nome:
    :return: certificado com nome
    """
    # PEGAR O 'BACKGOUND'
    base = Image.open(r"C:\Certificado_automatizado\Exemplo Certificado.png").convert("RGBA")

    # CRIAR UMA IMAGEM PRA DESENHAR POR CIMA
    txt = Image.new("RGBA", base.size, (255,255,255,0))

    # PEGAR A FONTE
    fonte = ImageFont.truetype(r"C:\Certificado_automatizado\playfair-display-black-italic.ttf", 96)

    # DESENAHR
    x = ImageDraw.Draw(txt)

    nome = nome.title()

    if len(nome) <= 14:
        #Desenhar texto full color
        x.text((700,550), f"{nome}", font = fonte, fill = (198,149,72,255))
    elif len(nome) > 14 and len(nome) <= 25:
        x.text((650, 550), f"{nome}", font=fonte, fill=(198,149,72, 255))
    else:
        x.text((500, 550), f"{nome}", font=fonte, fill=(198,149,72, 255))

    out = Image.alpha_composite(base, txt)

    nome = nome.replace(" ", "_")

    Image.alpha_composite(base, txt).save(f"Certificado_{nome}.png")

    out.show()




