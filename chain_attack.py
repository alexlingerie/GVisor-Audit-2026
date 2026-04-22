import subprocess
import os

def ejecutar_cadena():
    print("\x1b[34m[INIT]\x1b[0m Iniciando cadena de ataque ARCH-PROT-2025...")

    # 1. Simulamos la extracción del mensaje de error de Gerrit
    # En un ataque real, aquí harías una petición 'curl' al endpoint de Gerrit
    error_leak = "/data/data/com.termux/files/usr/bin/python3" # Simulación de Path Disclosure
    print(f"[+] Paso 1: Información filtrada de Gerrit -> {error_leak}")

    # 2. Automatizamos la inyección en el PoC de Node.js
    # Pasamos el leak como una variable de entorno para que el JS la capture
    print("[+] Paso 2: Inyectando metadatos en DigitalCredentialsService...")
    
    try:
        # Ejecutamos tu PoC de JS directamente desde Python
        resultado = subprocess.check_output(
            ["node", "arch_prot_2025.mjs"], 
            env={**os.environ, "LEAK_DATA": error_leak},
            stderr=subprocess.STDOUT
        )
        print("\x1b[32m[SUCCESS]\x1b[0m Respuesta del motor JS:")
        print(resultado.decode())
    except Exception as e:
        print(f"\x1b[31m[ERROR]\x1b[0m Falló la automatización: {e}")

if __name__ == "__main__":
    ejecutar_cadena()

