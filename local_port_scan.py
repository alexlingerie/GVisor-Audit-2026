import socket
from datetime import datetime

# Puertos críticos a auditar
# 22 (SSH), 80/443 (HTTP/S), 3306 (MySQL), 5432 (Postgres), 5555 (ADB over Wi-Fi), 8080 (Proxies/Dev)
target_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 5555, 6379, 8080, 9000, 9090]

target = "127.0.0.1"

print(f"📡 [ARCH-PROT-2025] Iniciando escaneo de puertos locales en ZTE...")
print(f"⏱️ Inicio: {datetime.now().strftime('%H:%M:%S')}\n")

for port in target_ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5) # Escaneo rápido
    result = s.connect_ex((target, port)) # Devuelve 0 si está abierto
    
    if result == 0:
        print(f"🚨 [ALERTA] Puerto {port:5} EXPUESTO (Abierto)")
        try:
            # Intentamos obtener un banner básico
            s.send(b"HEAD / HTTP/1.1\r\n\r\n")
            banner = s.recv(1024).decode().strip()
            if banner:
                print(f"   |_ Banner: {banner[:50]}...")
        except:
            pass
    s.close()

print(f"\n✅ Escaneo finalizado a las {datetime.now().strftime('%H:%M:%S')}")
