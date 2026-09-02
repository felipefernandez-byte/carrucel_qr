import json
from pathlib import Path
from urllib.parse import urlparse

ARCHIVO = Path("vercel.json")


def validar_url(url: str) -> str:
    url = url.strip()

    if not url:
        raise ValueError("La URL no puede estar vacía.")

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    parsed = urlparse(url)

    if not parsed.netloc:
        raise ValueError("La URL no es válida.")

    return url


if not ARCHIVO.exists():
    print("ERROR: No se encontró vercel.json en esta carpeta.")
    raise SystemExit(1)

config = json.loads(ARCHIVO.read_text(encoding="utf-8"))

redirects = config.get("redirects", [])

if not redirects:
    print("ERROR: vercel.json no contiene redirects.")
    raise SystemExit(1)

print("")
print("====================================================")
print("       CAMBIAR DESTINO DEL QR TPBV")
print("====================================================")
print("")

destino_actual = redirects[0].get("destination", "")
print("Destino actual:")
print(destino_actual)
print("")
print("Pega la NUEVA URL final.")
print("Puede ser Vercel, un dominio institucional, Google Forms, etc.")
print("")

nuevo = input("Nuevo destino: ")

try:
    nuevo = validar_url(nuevo)
except ValueError as exc:
    print("")
    print(f"ERROR: {exc}")
    raise SystemExit(1)

for redirect in redirects:
    if redirect.get("source") in ("/", "/qr"):
        redirect["destination"] = nuevo
        redirect["permanent"] = False

ARCHIVO.write_text(
    json.dumps(config, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8"
)

print("")
print("Destino actualizado correctamente:")
print(nuevo)
print("")
print("EL QR NO CAMBIÓ.")
print("")
print("Ahora sube el cambio:")
print('git add -A')
print('git commit -m "Actualizar destino del QR"')
print('git push')
print("")
