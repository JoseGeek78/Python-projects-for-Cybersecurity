import subprocess

perfil_red = input('Introduce el nombre del perfil de red WiFi: ')

try:
    
    resultados = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', perfil_red, 'key_clear'], shell=True).decode('utf-80', errors='backslashreplace')