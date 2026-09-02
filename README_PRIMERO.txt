QR TPBV - REDIRECCION V2 CORREGIDA
=====================================

OBJETIVO
--------
El QR de la lona apunta SIEMPRE a la URL estable de este mini proyecto en Vercel.
El destino final se puede cambiar cuando quieras SIN volver a generar ni imprimir el QR.

DESTINO ACTUAL
--------------
https://carrucel-tpbv.vercel.app/carrusel

PRIMERA VEZ - GENERAR EL QR
---------------------------
1. Confirma que este mini proyecto ya está publicado en Vercel.
2. Copia SU URL pública (la del mini proyecto redirector).
3. Instala qrcode si hace falta:
   python -m pip install "qrcode[pil]"
4. Ejecuta:
   python generar_qr_lona.py
5. El script te pedirá la URL del proyecto redirector.
6. Se crearán:
   qr_generado/QR_TPBV_LONA.png
   qr_generado/QR_TPBV_LONA.svg
   qr_generado/URL_FIJA_DEL_QR.txt

PARA CAMBIAR EL DESTINO DESPUÉS
-------------------------------
NO ejecutes generar_qr_lona.py otra vez.
NO cambies la lona.

Ejecuta:
   python cambiar_destino.py

Pega el nuevo destino, por ejemplo:
   https://nuevo-dominio.morelos.gob.mx/

Después:
   git add -A
   git commit -m "Actualizar destino del QR"
   git push

Vercel desplegará el cambio y EL MISMO QR abrirá el nuevo destino.

PRUEBA RÁPIDA
-------------
Puedes probar hoy cambiando temporalmente el destino a otra URL pública con:
   python cambiar_destino.py

Sube el cambio con git push y escanea EL MISMO QR.

Cuando termines la prueba, ejecuta otra vez cambiar_destino.py y vuelve a:
   https://carrucel-tpbv.vercel.app/carrusel

IMPORTANTE
----------
La URL que queda impresa dentro del QR debe ser la URL estable DEL MINI PROYECTO REDIRECTOR,
no la URL final del carrusel.
