import requests
import socket

# En gVisor, el acceso al Metadata Server suele estar restringido
target_dns = "metadata.google.internal"
target_ip = "169.254.169.254"

def audit_connection(host):
    print(f"🕵️ [GVISOR-AUDIT] Probando salida hacia: {host}")
    try:
        # Intentamos una conexión de bajo nivel
        s = socket.create_connection((host, 80), timeout=5)
        print(f"🚨 [ALERTA] Conexión establecida con {host}!")
        s.close()
    except socket.timeout:
        print(f"✅ [SAFE] Timeout: El sandbox está descartando los paquetes.")
    except Exception as e:
        print(f"🛡️ [INFO] Conexión rechazada: {e}")

print("📡 [ARCH-PROT-2025] Iniciando test de aislamiento de Red en gVisor...")
audit_connection(target_ip)
audit_connection(target_dns)

try:
    url = f"http://{target_ip}/computeMetadata/v1/instance/"
    headers = {"Metadata-Flavor": "Google"}
    r = requests.get(url, headers=headers, timeout=5)
    print(f"📊 Resultado HTTP: {r.status_code}")
except Exception as e:
    print(f"🔒 Bloqueo HTTP: {e}")

