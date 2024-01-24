import qrcode
import qrcode.image.svg
from qrcode.image.pure import PyPNGImage

class Qrcode:
    def __init__(self):
        pass

    def salvarPng(self,link,nome='Qrcode.png'):
        url = qrcode.make(link, image_factory=PyPNGImage)
        url.save(nome)

    def salvarSVG(self,link,nome='Qrcode.svg'):
        factory = qrcode.image.svg.SvgImage
        url = qrcode.make(link,image_factory=factory)
        url.save(nome)
