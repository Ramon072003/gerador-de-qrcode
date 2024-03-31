import qrcode
import qrcode.image.svg
from qrcode.image.pure import PyPNGImage
from PIL import Image

class Qrcode:
    def __init__(self):
        pass

    def salvarPng(self,link,nome):
        url = qrcode.make(link, image_factory=PyPNGImage)
        url.save(nome)
        imagem = Image.open(nome)
        imagem.show()

    def salvarSVG(self,link,nome):
        factory = qrcode.image.svg.SvgImage
        url = qrcode.make(link,image_factory=factory)
        url.save(nome)
