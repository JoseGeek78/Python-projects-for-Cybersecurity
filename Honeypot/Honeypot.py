# pip install paramiko

import socket
import threading
import logging

# Configuración del logging.
logging.basicConfig(filename='honeypot.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

# Clase para el Honeypot
class Honeypot:
    def __init__(self, host='0.0.0.0', port=2222):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Honeypot activo en {self.host}:{self.port}")

    def handle_client(self, client_socket, address):
        logging.info(f"Conexión establecida desde {address}")
        client_socket.send(b"SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.3\n")
        
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                logging.info(f"Datos recibidos de {address}: {data.decode('utf-8').strip()}")
                client_socket.send(b"Login incorrecto\n")
        except Exception as e:
            logging.error(f"Error manejando la conexión de {address}: {str(e)}")
        finally:
            client_socket.close()
            logging.info(f"Conexión cerrada desde {address}")

    def start(self):
        while True:
            client_socket, address = self.server_socket.accept()
            client_handler = threading.Thread(target=self.handle_client, args=(client_socket, address))
            client_handler.start()

if __name__ == "__main__":
    honeypot = Honeypot()
    honeypot.start()