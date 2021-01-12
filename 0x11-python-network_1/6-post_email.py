#!/usr/bin/python3
"""
script de Python que tome una URL y una dirección de correo electrónico,
envíe una POSTsolicitud a la URL pasada con el correo electrónico como
parámetro y finalmente muestre el cuerpo de la respuesta.
"""

import requests
import sys

if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    posted = r.text

    print(posted)
