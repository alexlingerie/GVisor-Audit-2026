import requests
import socket

target_local = "192.168.1.1" 
target_local_alt = "192.168.0.1"

def audit_connection(host):
    print(f"🕵️ [GVISOR-LATERAL] Auditando salto a red privada: {host}")
    try:
        s = socket.create_connection((host, 80), timeout=3)
        print(f"🚨 [ALERTA] Conexión abierta hacia {host}. ¡Aislamiento fallido!")
        s.close()
    except socket.timeout:
        print(f"✅ [SAFE] Timeout: El sandbox bloquea el tráfico lateral.")
    except Exception as e:
        print(f"🛡️ [INFO] Conexión denegada por el sistema: {e}")

print("📡 [ARCH-PROT-2025] Iniciando test de Movimiento Lateral...")
audit_connection(target_local)
audit_connection(target_local_alt)

try:
    r = requests.get(f"http://{target_local}", timeout=3)
    print(f"📊 Resultado HTTP: {r.status_code}")
except Exception as e:
    print(f"🔒 Bloqueo de capa de aplicación exitoso.")
