Network Scanner
Este proyecto incluye un script en Python que utiliza Nmap para escanear una red en busca de puertos abiertos, servicios y vulnerabilidades. El script está diseñado para ayudar a los profesionales de ciberseguridad a identificar posibles riesgos en sus redes.

Requisitos
Antes de ejecutar el script, asegúrate de tener instalados los siguientes componentes:

1. Python 3.x: Puedes descargarlo e instalarlo desde python.org.
2. Nmap: Instálalo desde nmap.org.
3. Librería python-nmap: Instálala usando pip:

----  pip install python-nmap  ----
 
Instalación de Nmap:

< En Windows >
1. Descarga el instalador de Nmap desde Nmap Download.
2. Ejecuta el instalador y sigue las instrucciones de instalación.
3. Verifica la instalación ejecutando nmap --version en PowerShell o el Símbolo del sistema.


< En Linux > (Debian/Ubuntu)
1. Actualiza los repositorios de paquetes:
sudo apt-get update
2. Instala Nmap:
sudo apt-get install nmap
3. Verifica la instalación ejecutando nmap --version en la Terminal.
nal.

--- Personalización:
Puedes cambiar el rango de IPs a escanear modificando la variable ip_range en el archivo network_scan.py: <br>
ip_range = '192.168.1.0/24'

Notas:
Asegúrate de tener permiso para escanear las redes objetivo. El uso no autorizado de herramientas de escaneo puede ser ilegal y contra las políticas de uso de la red.
Este script está diseñado para uso educativo y de prueba. No se recomienda su uso en entornos de producción sin una comprensión completa de las implicaciones y consecuencias.
Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para cualquier mejora o corrección.

Si tienes alguna pregunta o necesitas ayuda adicional, no dudes en abrir un issue en este repositorio.

Usa este script de forma responsable y legal.
