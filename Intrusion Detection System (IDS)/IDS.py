# pip install scapy
# pip install requests


from scapy.all import sniff, IP, TCP, UDP
from collections import defaultdict
import time

# Variables para detección de escaneo de puertos
port_scan_threshold = 10  # Número de puertos a los que se puede conectar una IP en un intervalo de tiempo
port_scan_time_window = 60  # Intervalo de tiempo en segundos
connection_attempts = defaultdict(list)

# Variables para detección de ataques brute force
brute_force_threshold = 5  # Número de intentos fallidos de conexión
brute_force_time_window = 60  # Intervalo de tiempo en segundos
failed_login_attempts = defaultdict(list)

# Payloads conocidos de ataques
known_attack_payloads = [
    b'\x90\x90\x90\x90',  # NOP sled (ejemplo de patrón de buffer overflow)
    b'admin',  # Intento de login con credenciales conocidas
    b'<?php',  # Intento de inyección de código PHP
]

def detect_suspicious_activity(packet):
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        
        if packet.haslayer(TCP):
            tcp_sport = packet[TCP].sport
            tcp_dport = packet[TCP].dport
            
            # Regla: Detectar tráfico HTTP/HTTPS
            if tcp_dport in [80, 443]:
                print(f"Alerta: tráfico HTTP/HTTPS detectado desde {ip_src}:{tcp_sport} hacia {ip_dst}:{tcp_dport}")
            
            # Regla: Detección de escaneo de puertos
            current_time = time.time()
            connection_attempts[ip_src].append(current_time)
            connection_attempts[ip_src] = [t for t in connection_attempts[ip_src] if current_time - t < port_scan_time_window]
            
            if len(connection_attempts[ip_src]) > port_scan_threshold:
                print(f"Alerta: posible escaneo de puertos detectado desde {ip_src}")

            # Regla: Detección de ataques brute force (suponiendo que se detectan intentos fallidos de conexión)
            # Aquí solo como ejemplo, en un caso real necesitarías integrarte con un sistema de autenticación
            if "failed login" in str(packet):
                failed_login_attempts[ip_src].append(current_time)
                failed_login_attempts[ip_src] = [t for t in failed_login_attempts[ip_src] if current_time - t < brute_force_time_window]
                
                if len(failed_login_attempts[ip_src]) > brute_force_threshold:
                    print(f"Alerta: posible ataque brute force detectado desde {ip_src}")

            # Regla: Detección de payloads sospechosos
            if any(payload in bytes(packet[TCP].payload) for payload in known_attack_payloads):
                print(f"Alerta: payload sospechoso detectado desde {ip_src} hacia {ip_dst}:{tcp_dport}")

        if packet.haslayer(UDP):
            udp_sport = packet[UDP].sport
            udp_dport = packet[UDP].dport
            
            # Regla: Detectar tráfico DNS
            if udp_dport == 53:
                print(f"Alerta: tráfico DNS detectado desde {ip_src}:{udp_sport} hacia {ip_dst}:{udp_dport}")

# Función de captura de paquetes
def packet_callback(packet):
    detect_suspicious_activity(packet)

# Iniciar la captura de paquetes
print("Iniciando IDS...")
sniff(prn=packet_callback, store=0)

mm mm mm