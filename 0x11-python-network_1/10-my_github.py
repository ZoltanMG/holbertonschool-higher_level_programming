#!/usr/bin/python3
"""
script de Python que tome sus credenciales de Github (nombre de usuario y
contraseña) y use la API de Github para mostrar su id
"""

import requests
import sys

if __name__ == "__main__":
    # Get the info requesting the api
    user = sys.argv[1]
    passw = sys.argv[2]
    url = 'https://api.github.com/users/{}'.format(user)

    response = requests.get(url, auth=(user, passw))

    try:
        print(response.json()['id'])
    except KeyError:
        print("None")
