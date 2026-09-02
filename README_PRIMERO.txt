QR TPBV - PROYECTO DE REDIRECCION
====================================

OBJETIVO
--------
Este proyecto existe únicamente para que el QR impreso en las lonas nunca tenga que cambiar.

FLUJO
-----
QR impreso
  -> URL fija de este proyecto Vercel
  -> destino configurado en vercel.json

DESTINO ACTUAL
--------------
https://carrucel-tpbv.vercel.app/carrusel

COMO CAMBIAR EL DESTINO EN EL FUTURO
------------------------------------
Abre vercel.json y cambia SOLO el valor de "destination".

Ejemplo actual:
"destination": "https://carrucel-tpbv.vercel.app/carrusel"

Ejemplo futuro:
"destination": "https://otro-proyecto.vercel.app/"

Después:
git add -A
git commit -m "Cambiar destino QR"
git push

El QR impreso NO cambia.

PRIMERA PUBLICACION
-------------------
1. Descomprime este proyecto.
2. Abre PowerShell dentro de la carpeta.
3. Si quieres usar Git:
   git init
   git add -A
   git commit -m "Proyecto inicial QR TPBV"

4. Publica en Vercel:
   npx vercel

5. Cuando Vercel te dé la URL definitiva, por ejemplo:
   https://qr-tpbv.vercel.app/

6. Abre generar_qr_lona.py y coloca ESA URL en:
   URL_QR = "https://qr-tpbv.vercel.app/"

7. Instala la librería QR si hace falta:
   python -m pip install "qrcode[pil]"

8. Genera el QR:
   python generar_qr_lona.py

9. Prueba el QR con varios celulares antes de mandar a imprimir.

IMPORTANTE
----------
No imprimas el QR hasta confirmar cuál será la URL definitiva del nuevo proyecto en Vercel.
Una vez impreso, conserva esa URL del proyecto.
