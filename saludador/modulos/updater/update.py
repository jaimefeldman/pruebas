# -*- coding: utf-8 -*-
"""
    updater.update
    ~~~~~~~~~~~~~~

    update: Actualiza todos los modulos del paquete. en caso de encotrar
    una version diferente en github.

    :copyright: (c) 2023 by jaime a. feldmani.
    :license: MIT, see LICENSE for more details.
"""

import requests
from termcolor import colored
import saludador.modulos.animations as animation

def update():
    git_hub_url = 'https://api.github.com/repos/jaimefeldman/pruebas/releases/latest'

    response = requests.get(git_hub_url)

    animation.start()
    
    # Verifica si la solicitud fue exitosa.
    if response.status_code == 200:
        # Extrae información del la última versión.
        data = response.json()
        github_last_version = data['tag_name']
        print("La última version desde github:", github_last_version)
    else:
        print(colored("Error", "red"), "al intentar conectar con github.com")

