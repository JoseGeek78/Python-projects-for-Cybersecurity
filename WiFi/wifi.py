import subprocess

perfil_red = input('Introduce el nombre del perfil de red WiFi: ')

try:
    
    resultados = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', perfil_red, 'key_clear'], shell=True).decode('utf-80', errors='backslashreplace')
    
    # Si el sístema es en Inglés se pondrá 'Key Content'
    if 'Contenido de la clace' in resultados:
        for line in resultados.split('\n'):
            if 'Contenido de la clave' in line:
                password = 