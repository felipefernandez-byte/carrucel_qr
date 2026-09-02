from pathlib import Path

import qrcode
from qrcode.constants import ERROR_CORRECT_H
from qrcode.image.svg import SvgPathImage


# ============================================================
# URL FIJA DEL PROYECTO REDIRECTOR
# ============================================================

URL_QR = "https://carrucel-qr.vercel.app/"


# ============================================================
# RUTA DEL PROYECTO
# ============================================================

# Carpeta exacta donde está este archivo Python
BASE_DIR = Path(__file__).resolve().parent

# Carpeta de salida DENTRO del proyecto
CARPETA_SALIDA = BASE_DIR / "qr_generado"

CARPETA_SALIDA.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# ARCHIVOS
# ============================================================

ARCHIVO_PNG = CARPETA_SALIDA / "QR_TPBV_LONA.png"
ARCHIVO_SVG = CARPETA_SALIDA / "QR_TPBV_LONA.svg"
ARCHIVO_TXT = CARPETA_SALIDA / "URL_FIJA_DEL_QR.txt"


# ============================================================
# GENERAR QR
# ============================================================

qr = qrcode.QRCode(
    version=None,
    error_correction=ERROR_CORRECT_H,
    box_size=32,
    border=4
)

qr.add_data(URL_QR)
qr.make(fit=True)


# ============================================================
# PNG
# ============================================================

imagen_png = qr.make_image(
    fill_color="black",
    back_color="white"
)

imagen_png.save(str(ARCHIVO_PNG))


# ============================================================
# SVG
# ============================================================

imagen_svg = qr.make_image(
    image_factory=SvgPathImage
)

imagen_svg.save(str(ARCHIVO_SVG))


# ============================================================
# TXT DE CONTROL
# ============================================================

ARCHIVO_TXT.write_text(
    f"URL FIJA DEL QR:\n{URL_QR}\n",
    encoding="utf-8"
)


# ============================================================
# VERIFICAR QUE REALMENTE EXISTEN
# ============================================================

print("")
print("==============================================")
print(" QR TPBV GENERADO")
print("==============================================")
print("")

print("URL contenida:")
print(URL_QR)

print("")
print("Carpeta de salida:")
print(CARPETA_SALIDA)

print("")
print("PNG:")
print(ARCHIVO_PNG)
print("Existe:", ARCHIVO_PNG.exists())

print("")
print("SVG:")
print(ARCHIVO_SVG)
print("Existe:", ARCHIVO_SVG.exists())

print("")
print("TXT:")
print(ARCHIVO_TXT)
print("Existe:", ARCHIVO_TXT.exists())

print("")
print("==============================================")