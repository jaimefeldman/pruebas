# -*- coding: utf-8 -*-
"""
    updater.update
    ~~~~~~~~~~~~~~

    update: Actualiza todos los modulos del paquete. en caso de encotrar
    una version diferente en github.

    :copyright: (c) 2023 by jaime a. feldmani.
    :license: MIT, see LICENSE for more details.
"""

import requests, time
from termcolor import colored
from halo import Halo


def update():
    git_hub_url = 'https://api.github.com/repos/jaimefeldman/pruebas/releases/latest'
    
    spinner = Halo(text='Checking for updates...', text_color='cyan', color='yellow', spinner='dots')

    try:
        spinner.start() 
        response = requests.get(git_hub_url)
        time.sleep(3)
    except (KeyboardInterrupt, SystemExit):
        spinner.stop()
        sys.exit(1)

    # Verifica si la solicitud fue exitosa.
    if response.status_code == 200:
        # Extrae información del la última versión.
        data = response.json()
        github_last_version = data['tag_name']
        spinner.succeed('the app is already updated!')
        spinner.stop()
    else:

        spinner.fail("Error: al intentar conectar con github.com")
        spinner.stop()

