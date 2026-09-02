from pathlib import Path

import qrcode
from qrcode.constants import ERROR_CORRECT_H
from qrcode.image.svg import SvgPathImage


# ============================================================
# URL REAL DEL CARRUSEL
# ============================================================

URL_QR = "https://carrucel-tpbv.vercel.app/"


# ============================================================
# CARPETA DONDE SE GUARDARÁ EL QR
# ============================================================

carpeta_salida = Path("qr_generado")

carpeta_salida.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# ARCHIVOS DE SALIDA
# ============================================================

archivo_png = carpeta_salida / "QR_TPBV_LONA.png"
archivo_svg = carpeta_salida / "QR_TPBV_LONA.svg"


# ============================================================
# CONFIGURACIÓN DEL QR
# ============================================================

qr = qrcode.QRCode(

    # Tamaño automático
    version=None,

    # Corrección de errores alta
    # Recomendable para impresión en lona
    error_correction=ERROR_CORRECT_H,

    # Resolución del PNG
    box_size=32,

    # Margen blanco
    border=4
)


# Agregar URL al QR
qr.add_data(URL_QR)

# Crear QR
qr.make(fit=True)


# ============================================================
# GENERAR PNG
# ============================================================

imagen_png = qr.make_image(
    fill_color="black",
    back_color="white"
)

imagen_png.save(archivo_png)


# ============================================================
# GENERAR SVG
# ============================================================

imagen_svg = qr.make_image(
    image_factory=SvgPathImage
)

imagen_svg.save(archivo_svg)


# ============================================================
# RESULTADO
# ============================================================

print("")
print("================================================")
print("       QR TPBV GENERADO CORRECTAMENTE")
print("================================================")
print("")

print("URL incluida en el QR:")
print(URL_QR)

print("")
print("PNG:")
print(archivo_png.resolve())

print("")
print("SVG:")
print(archivo_svg.resolve())

print("")
print("IMPORTANTE:")
print("Para impresión en lona utiliza preferentemente el SVG.")
print("")