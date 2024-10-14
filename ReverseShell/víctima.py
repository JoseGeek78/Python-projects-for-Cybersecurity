from socket import socket
from subprocess import getoutput
from os import chdir, getcwd
from time import sleep

# Definimos la dirección y puerto, la direcion 0.0.0.0 hace referencia a que aceptamos conexiones de cualquier interfaz
server_address = ('0.0.0.0', 5000)...