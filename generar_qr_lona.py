from pathlib import Path
import qrcode
from qrcode.constants import ERROR_CORRECT_H
from qrcode.image.svg import SvgPathImage

# Cambia esta URL UNA SOLA VEZ después de publicar este proyecto en Vercel.
# Después de imprimir las lonas, NO cambies esta URL.
URL_QR = "https://qr-tpbv.vercel.app/"

salida = Path("qr_generado")
salida.mkdir(parents=True, exist_ok=True)

png_path = salida / "QR_TPBV_LONA.png"
svg_path = salida / "QR_TPBV_LONA.svg"

qr = qrcode.QRCode(
    version=None,
    error_correction=ERROR_CORRECT_H,
    box_size=32,
    border=4,
)
qr.add_data(URL_QR)
qr.make(fit=True)

img_png = qr.make_image(fill_color="black", back_color="white")
img_png.save(png_path)

img_svg = qr.make_image(image_factory=SvgPathImage)
img_svg.save(svg_path)

print("")
print("======================================")
print(" QR TPBV GENERADO CORRECTAMENTE")
print("======================================")
print("URL fija:", URL_QR)
print("PNG:", png_path.resolve())
print("SVG:", svg_path.resolve())
print("")
print("Para lona utiliza preferentemente el archivo SVG.")
