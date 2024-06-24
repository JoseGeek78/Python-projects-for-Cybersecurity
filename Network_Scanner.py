import nmap

def scan_network(ip_range):
    # Crear un objeto de escáner
    nm = nmap.PortScanner()
    
    # Escanear el rango de IPs con detección de versiones y vulnerabilidades
    print(f"Escaneando la red en el rango: {ip_range}")
    nm.scan(hosts=ip_range, arguments='-sV --script=vuln')
    
    # Iterar sobre todos los hosts encontrados
    for host in nm.all_hosts():
        print(f"\nHost: {host} ({nm[host].hostname()})")
        print(f"Estado: {nm[host].state()}")
        
        # Iterar sobre todos los protocolos (TCP/UDP) detectados en el host
        for proto in nm[host].all_protocols():
            print(f"\nProtocolo: {proto}")
            
            # Obtener todos los puertos abiertos
            lport = nm[host][proto].keys()
            for port in lport:
                print(f"Puerto: {port}\tEstado: {nm[host][proto][port]['state']}\tServicio: {nm[host][proto][port]['name']}")
                
                # Mostrar información adicional si está disponible
                if 'version' in nm[host][proto][port]:
                    print(f"\tVersión: {nm[host][proto][port]['version']}")
                if 'product' in nm[host][proto][port]:
                    print(f"\tProducto: {nm[host][proto][port]['product']}")
                
                # Mostrar vulnerabilidades encontradas
                if 'script' in nm[host][proto][port]:
                    for script in nm[host][proto][port]['script']:
                        print(f"\n[VULNERABILIDAD] {script}:\n{nm[host][proto][port]['script'][script]}")

if __name__ == "__main__":
    # Rango de IPs a escanear (puedes cambiarlo por el rango que desees, o dejarlo como está, a mí plim)
    ip_range = '192.168.1.0/24'
    
    scan_network(ip_range)
        
  