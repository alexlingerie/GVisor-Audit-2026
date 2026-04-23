import os
import requests
import sys

def fast_audit():
    limit = 32765
    fds = []
    print("--- [ARCH-PROT-2025] Sonda de Precision ---")
    
    try:
        print("[*] Saturando descriptores...")
        for i in range(limit):
            fds.append(os.open('/dev/null', os.O_RDONLY))
        
        print("[!] Sistema saturado. Intentando peticion de red...")
        r = requests.get("https://www.googleapis.com/oauth2/v3/tokeninfo", timeout=2)
        print(f"Resultado: {r.status_code}")
        
    except Exception as e:
        print(f"\n[EVIDENCIA OBTENIDA]:\n{e}")
    finally:
        # Limpieza para no dejar el sistema inestable
        for f in fds:
            os.close(f)

if __name__ == "__main__":
    fast_audit()
